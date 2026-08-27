const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname);
const VIEWERS_DIR = '.viewers';
const EXCLUDE_DIRS = ['.git', 'node_modules', '.idea', '.vscode', 'venv', '.viewers', 'dist', 'build'];

// Helper to escape HTML
function escapeHtml(str) {
  if (!str) return '';
  return str
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

// Format bytes
function formatBytes(bytes, decimals = 1) {
  if (!+bytes) return '0 B';
  const k = 1024;
  const dm = decimals < 0 ? 0 : decimals;
  const sizes = ['B', 'KB', 'MB', 'GB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return `${parseFloat((bytes / Math.pow(k, i)).toFixed(dm))} ${sizes[i]}`;
}

// Category detector
function detectCategory(relPath) {
  const normalized = relPath.replace(/\\/g, '/').toLowerCase();
  if (normalized.startsWith('resumos')) return 'Resumos Jupyter';
  if (normalized.startsWith('jornada python')) return 'Jornada Python';
  if (normalized.startsWith('cursoemvideo_python')) return 'Curso em Vídeo';
  if (normalized.startsWith('cisco_fundamentos_python')) return 'Cisco Python';
  if (normalized.startsWith('mimo_app')) return 'Mimo App';
  if (normalized.startsWith('javascript')) return 'JavaScript & Web';
  if (normalized.startsWith('python')) return 'Apostilas & PDFs';
  return 'Geral';
}

// Build file tree
function buildFileTree(startPath) {
  const viewersDirPath = path.join(startPath, VIEWERS_DIR);
  if (fs.existsSync(viewersDirPath)) {
    fs.rmSync(viewersDirPath, { recursive: true, force: true });
  }
  fs.mkdirSync(viewersDirPath, { recursive: true });

  const tree = {
    name: path.basename(startPath),
    type: 'folder',
    path: '',
    children: []
  };

  const allFilesList = [];

  function walk(currentDir, parentNode) {
    const items = fs.readdirSync(currentDir).sort((a, b) => {
      const pA = path.join(currentDir, a);
      const pB = path.join(currentDir, b);
      const isDirA = fs.statSync(pA).isDirectory();
      const isDirB = fs.statSync(pB).isDirectory();
      if (isDirA && !isDirB) return -1;
      if (!isDirA && isDirB) return 1;
      return a.localeCompare(b, undefined, { numeric: true, sensitivity: 'base' });
    });

    for (const item of items) {
      if (EXCLUDE_DIRS.includes(item)) continue;

      const fullPath = path.join(currentDir, item);
      const relPath = path.relative(startPath, fullPath);
      const stat = fs.statSync(fullPath);

      if (stat.isDirectory()) {
        const folderNode = {
          name: item,
          type: 'folder',
          path: relPath.replace(/\\/g, '/'),
          children: []
        };
        parentNode.children.push(folderNode);
        walk(fullPath, folderNode);
      } else {
        if (['build_dashboard.py', 'build_dashboard.js', '.gitignore', 'index.html'].includes(item)) {
          continue;
        }

        const ext = path.extname(item).toLowerCase();
        const normRelPath = relPath.replace(/\\/g, '/');
        const category = detectCategory(relPath);

        // Generate static viewer HTML for fallback / direct URL opening
        const viewerFileName = relPath.replace(/[^a-zA-Z0-9]/g, '_') + '.html';
        const viewerPath = path.join(viewersDirPath, viewerFileName);
        const viewerUrl = `${VIEWERS_DIR}/${viewerFileName}`;

        const fileInfo = {
          name: item,
          type: 'file',
          ext: ext,
          path: normRelPath,
          viewerUrl: viewerUrl,
          size: stat.size,
          sizeFormatted: formatBytes(stat.size),
          modified: stat.mtimeMs,
          category: category
        };

        parentNode.children.push(fileInfo);
        allFilesList.push(fileInfo);

        // Create standalone fallback viewer
        generateStandaloneViewer(fullPath, relPath, viewerPath, item, ext);
      }
    }
  }

  walk(startPath, tree);
  return { tree, allFilesList };
}

// Generate standalone viewer
function generateStandaloneViewer(filePath, relPath, viewerPath, title, ext) {
  try {
    let contentHtml = '';
    let extraHead = '';
    const normRelPath = '../' + relPath.replace(/\\/g, '/');

    if (ext === '.py') {
      const code = fs.readFileSync(filePath, 'utf-8');
      extraHead = `
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/styles/atom-one-dark.min.css">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/highlight.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/languages/python.min.js"></script>
        <style>
          pre { border-radius: 8px; overflow-x: auto; font-size: 0.95rem; }
          .code-toolbar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem; }
          .btn-copy { background: rgba(56, 189, 248, 0.2); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.4); padding: 0.4rem 0.8rem; border-radius: 6px; cursor: pointer; font-size: 0.85rem; }
          .btn-copy:hover { background: rgba(56, 189, 248, 0.4); }
        </style>
      `;
      contentHtml = `
        <div class="container">
          <div class="code-toolbar">
            <span style="color: #38bdf8; font-weight: 600;"><i class="fa-brands fa-python"></i> ${escapeHtml(title)}</span>
            <button class="btn-copy" onclick="navigator.clipboard.writeText(document.getElementById('py-code').innerText); this.innerText='Copiado!'; setTimeout(()=>this.innerText='Copiar Código', 2000)"><i class="fa-regular fa-copy"></i> Copiar Código</button>
          </div>
          <pre><code class="language-python" id="py-code">${escapeHtml(code)}</code></pre>
        </div>
        <script>hljs.highlightAll();</script>
      `;
    } else if (ext === '.ipynb') {
      let notebook = { cells: [] };
      try {
        notebook = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
      } catch (e) {
        notebook = { cells: [] };
      }
      extraHead = `
        <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/styles/atom-one-dark.min.css">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/highlight.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/languages/python.min.js"></script>
        <style>
          .cell { margin-bottom: 1.5rem; }
          .cell-markdown { font-size: 1.05rem; line-height: 1.6; color: #cbd5e1; }
          .cell-markdown h1, .cell-markdown h2, .cell-markdown h3 { color: #f1f5f9; margin-top: 1rem; margin-bottom: 0.5rem; }
          .cell-markdown code { background: rgba(0,0,0,0.3); padding: 0.2rem 0.4rem; border-radius: 4px; color: #eab308; }
          .cell-markdown pre { background: rgba(0,0,0,0.3); padding: 1rem; border-radius: 8px; overflow-x: auto; border: 1px solid var(--glass-border); margin: 1rem 0; }
          .cell-code { background: #1e293b; border-radius: 8px; padding: 1rem; overflow-x: auto; position: relative; border: 1px solid var(--glass-border); }
          .cell-output { background: #0f172a; color: #a3e635; padding: 1rem; border-radius: 8px; margin-top: 0.5rem; font-family: monospace; overflow-x: auto; white-space: pre-wrap; font-size: 0.9rem; }
          .prompt { position: absolute; top: 0.5rem; right: 0.5rem; color: #64748b; font-size: 0.75rem; }
        </style>
      `;

      let cellsHtml = '';
      (notebook.cells || []).forEach((cell, idx) => {
        const source = Array.isArray(cell.source) ? cell.source.join('') : (cell.source || '');
        if (cell.cell_type === 'markdown') {
          const b64 = Buffer.from(source).toString('base64');
          cellsHtml += `
            <div class="cell cell-markdown" id="md-${idx}"></div>
            <script>
              document.getElementById('md-${idx}').innerHTML = marked.parse(decodeURIComponent(escape(window.atob('${b64}'))));
            </script>
          `;
        } else if (cell.cell_type === 'code') {
          cellsHtml += `
            <div class="cell cell-code">
              <div class="prompt">In [${cell.execution_count || ' '}]</div>
              <pre><code class="language-python">${escapeHtml(source)}</code></pre>
            </div>
          `;
          const outputs = cell.outputs || [];
          if (outputs.length > 0) {
            let outText = '';
            outputs.forEach(out => {
              if (out.output_type === 'stream') {
                outText += Array.isArray(out.text) ? out.text.join('') : (out.text || '');
              } else if (out.output_type === 'execute_result' || out.output_type === 'display_data') {
                if (out.data && out.data['text/plain']) {
                  const plain = out.data['text/plain'];
                  outText += Array.isArray(plain) ? plain.join('') : plain;
                }
              }
            });
            if (outText.trim()) {
              cellsHtml += `<div class="cell-output">${escapeHtml(outText)}</div>`;
            }
          }
        }
      });

      contentHtml = `<div class="container">${cellsHtml}</div><script>hljs.highlightAll();</script>`;
    } else if (ext === '.md') {
      const source = fs.readFileSync(filePath, 'utf-8');
      const b64 = Buffer.from(source).toString('base64');
      extraHead = `
        <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/styles/atom-one-dark.min.css">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/highlight.min.js"></script>
        <style>
          .markdown-body { font-size: 1.05rem; line-height: 1.7; color: #cbd5e1; }
          .markdown-body h1, .markdown-body h2 { border-bottom: 1px solid var(--glass-border); padding-bottom: 0.5rem; margin-bottom: 1rem; color: #38bdf8; }
          .markdown-body a { color: #38bdf8; text-decoration: none; }
          .markdown-body a:hover { text-decoration: underline; }
          .markdown-body pre { background: #1e293b; padding: 1rem; border-radius: 8px; overflow-x: auto; border: 1px solid var(--glass-border); margin: 1rem 0; }
          .markdown-body code { font-family: monospace; color: #eab308; background: rgba(0,0,0,0.3); padding: 0.2rem 0.4rem; border-radius: 4px; }
          .markdown-body pre code { padding: 0; background: transparent; color: inherit; }
          .markdown-body img { max-width: 100%; border-radius: 8px; }
          table { border-collapse: collapse; width: 100%; margin: 1rem 0; }
          th, td { border: 1px solid var(--glass-border); padding: 0.6rem; text-align: left; }
          th { background: rgba(255,255,255,0.05); color: #38bdf8; }
        </style>
      `;
      contentHtml = `
        <div class="container markdown-body" id="md-content"></div>
        <script>
          document.getElementById('md-content').innerHTML = marked.parse(decodeURIComponent(escape(window.atob('${b64}'))));
          hljs.highlightAll();
        </script>
      `;
    } else if (ext === '.pdf') {
      extraHead = `
        <style>
          main { padding: 0 !important; max-width: 100% !important; height: calc(100vh - 75px); }
          .pdf-container { width: 100%; height: 100%; }
          iframe { width: 100%; height: 100%; border: none; }
        </style>
      `;
      contentHtml = `<div class="pdf-container"><iframe src="${normRelPath}"></iframe></div>`;
    } else {
      contentHtml = `<div class="container"><p>Abrindo arquivo: <a href="${normRelPath}" target="_blank" style="color:#38bdf8">${escapeHtml(title)}</a></p></div>`;
    }

    const htmlDoc = `<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${escapeHtml(title)} - Meus Estudos</title>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  ${extraHead}
  <style>
    :root {
      --bg-color: #0b1120;
      --glass-bg: rgba(30, 41, 59, 0.7);
      --glass-border: rgba(255, 255, 255, 0.08);
      --primary: #38bdf8;
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
    }
    * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Outfit', sans-serif; }
    body { background-color: var(--bg-color); color: var(--text-main); min-height: 100vh; display: flex; flex-direction: column; }
    header { padding: 0.8rem 2rem; display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid var(--glass-border); background: var(--glass-bg); backdrop-filter: blur(12px); position: sticky; top: 0; z-index: 100; }
    .header-left { display: flex; align-items: center; gap: 1rem; }
    .back-btn { color: var(--text-main); text-decoration: none; display: flex; align-items: center; gap: 0.5rem; padding: 0.5rem 1rem; border-radius: 8px; background: rgba(255,255,255,0.05); font-size: 0.9rem; transition: 0.2s; }
    .back-btn:hover { background: rgba(56, 189, 248, 0.2); color: var(--primary); }
    .file-title { font-size: 1.1rem; font-weight: 600; color: #f8fafc; }
    main { flex: 1; padding: 2rem; max-width: 1200px; margin: 0 auto; width: 100%; }
    .container { background: rgba(15, 23, 42, 0.7); border: 1px solid var(--glass-border); border-radius: 16px; padding: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.3); overflow-x: auto; }
  </style>
</head>
<body>
  <header>
    <div class="header-left">
      <a href="../index.html" class="back-btn"><i class="fa-solid fa-arrow-left"></i> Voltar ao Dashboard</a>
      <div class="file-title">${escapeHtml(title)}</div>
    </div>
    <div>
      <a href="${normRelPath}" download class="back-btn"><i class="fa-solid fa-download"></i> Baixar Arquivo</a>
    </div>
  </header>
  <main>
    ${contentHtml}
  </main>
</body>
</html>`;

    fs.writeFileSync(viewerPath, htmlDoc, 'utf-8');
  } catch (err) {
    console.error(`Erro ao gerar viewer para ${filePath}:`, err.message);
  }
}

// Built-in Quizzes Data
const QUIZZES_DATA = [
  {
    id: "mod-01",
    title: "Módulo 01: Introdução & Filosofia Python",
    questions: [
      {
        question: "Quem criou a linguagem Python e em que ano ela foi lançada pela primeira vez?",
        options: ["Guido van Rossum (1991)", "Brendan Eich (1995)", "James Gosling (1995)", "Dennis Ritchie (1972)"],
        answer: 0,
        explanation: "Python foi concebido no final dos anos 1980 por Guido van Rossum no CWI e lançado em 1991."
      },
      {
        question: "Qual comando no terminal Python exibe o manifesto 'The Zen of Python'?",
        options: ["import zen", "import this", "help(python)", "python --philosophy"],
        answer: 1,
        explanation: "'import this' é o easter egg clássico que imprime os 19 aforismos do Zen do Python escritos por Tim Peters."
      },
      {
        question: "Como o Python define blocos de código (como funções, loops e condicionais)?",
        options: ["Chaves { }", "Palavras-chave begin / end", "Indentação consistente (espaços/tabs)", "Ponto e vírgula ;"],
        answer: 2,
        explanation: "Em Python, a indentação obrigatória é parte da sintaxe e determina o escopo e blocos de código."
      }
    ]
  },
  {
    id: "mod-02",
    title: "Módulo 02: Variáveis & Tipagem Dinâmica",
    questions: [
      {
        question: "Qual das seguintes convenções de nomenclatura é a recomendada pela PEP 8 para variáveis e funções?",
        options: ["camelCase", "PascalCase", "snake_case", "kebab-case"],
        answer: 2,
        explanation: "A PEP 8 recomenda snake_case (letras minúsculas separadas por underline) para nomes de variáveis e funções."
      },
      {
        question: "O que a tipagem dinâmica e forte em Python significa na prática?",
        options: [
          "O tipo da variável é fixo na declaração e converte automaticamente strings em inteiros",
          "O tipo é inferido em tempo de execução, mas operações inválidas entre tipos incompatíveis geram TypeError",
          "Não existem tipos primitivos em Python",
          "Todas as variáveis devem ser precedidas de 'var' ou 'let'"
        ],
        answer: 1,
        explanation: "Dinâmica = você não declara tipos manualmente; Forte = Python não faz coerções implícitas perigosas (ex: '5' + 2 gera erro)."
      },
      {
        question: "Qual função embutida retorna o identificador único de memória de um objeto?",
        options: ["type()", "memory()", "id()", "ref()"],
        answer: 2,
        explanation: "A função id(objeto) retorna o endereço de memória / identidade única do objeto em tempo de execução."
      }
    ]
  },
  {
    id: "mod-03",
    title: "Módulo 03: Tipos Primitivos & Conversões",
    questions: [
      {
        question: "Qual é o resultado da expressão type(4 / 2) em Python 3?",
        options: ["<class 'int'>", "<class 'float'>", "<class 'number'>", "<class 'double'>"],
        answer: 1,
        explanation: "O operador '/' (divisão padrão) em Python 3 sempre retorna um float (2.0), mesmo que a divisão seja exata."
      },
      {
        question: "Qual operador realiza a divisão inteira (piso da divisão)?",
        options: ["//", "%", "div()", "int(/)"],
        answer: 0,
        explanation: "O operador '//' descarta a parte fracionária e retorna o quociente inteiro (ex: 7 // 2 = 3)."
      },
      {
        question: "Qual dos seguintes valores é avaliado como False em contexto booleano (falsy)?",
        options: ["'0'", "[] (lista vazia)", "[False]", "-1"],
        answer: 1,
        explanation: "Coleções vazias ([], {}, ()), 0, 0.0, None e string vazia '' são avaliados como False."
      }
    ]
  },
  {
    id: "mod-04",
    title: "Módulo 04: Operadores Lógicos e de Comparação",
    questions: [
      {
        question: "Qual é a diferença entre '==' e 'is' em Python?",
        options: [
          "'==' compara valores/conteúdo, enquanto 'is' verifica se ambas variáveis apontam para o mesmo objeto na memória",
          "Não há diferença, são sinônimos",
          "'is' é apenas para números inteiros",
          "'==' é para tipos primitivos e 'is' para strings"
        ],
        answer: 0,
        explanation: "'==' verifica igualdade de valor (__eq__), enquanto 'is' verifica identidade de endereço de memória (id(a) == id(b))."
      },
      {
        question: "Qual o resultado da avaliação 'Python' and 'Rocks'?",
        options: ["True", "'Python'", "'Rocks'", "False"],
        answer: 2,
        explanation: "O operador 'and' em Python utiliza curto-circuito: se o primeiro operando for truthy, ele retorna o segundo operando."
      }
    ]
  },
  {
    id: "mod-05",
    title: "Módulo 05: Estruturas de Dados (Listas, Tuplas, Dicionários)",
    questions: [
      {
        question: "Qual a principal diferença entre uma Lista (list) e uma Tupla (tuple)?",
        options: [
          "Listas são mutáveis e Tuplas são imutáveis",
          "Tuplas podem conter apenas números",
          "Listas usam parênteses () e Tuplas usam colchetes []",
          "Não há diferença de performance nem de mutabilidade"
        ],
        answer: 0,
        explanation: "Listas podem ser alteradas (append, pop, alteração de índices), enquanto tuplas são imutáveis e mais leves."
      },
      {
        question: "Qual método do dicionário permite buscar um valor por chave com um valor padrão caso a chave não exista?",
        options: ["dict.find(key, default)", "dict.get(key, default)", "dict.search(key)", "dict.fetch(key)"],
        answer: 1,
        explanation: "dict.get(chave, valor_padrao) evita que o programa lance um KeyError caso a chave não esteja presente."
      },
      {
        question: "O que a sintaxe `[x**2 for x in range(5) if x % 2 == 0]` produz?",
        options: ["[0, 4, 16]", "[1, 9]", "[0, 1, 4, 9, 16]", "[4, 16]"],
        answer: 0,
        explanation: "Para x em [0, 1, 2, 3, 4], os pares são 0, 2, 4. Seus quadrados são 0, 4, 16."
      }
    ]
  },
  {
    id: "mod-06",
    title: "Módulo 06: Funções, *args e **kwargs",
    questions: [
      {
        question: "O que o parâmetro `*args` recebe dentro de uma função Python?",
        options: [
          "Uma tupla com todos os argumentos posicionais excedentes",
          "Um dicionário com argumentos nomeados",
          "Uma lista de ponteiros",
          "Uma string concatenada"
        ],
        answer: 0,
        explanation: "`*args` empacota múltiplos argumentos posicionais em uma tupla imutável."
      },
      {
        question: "Como se chama uma função anônima de linha única em Python?",
        options: ["arrow function", "lambda function", "inline def", "closure"],
        answer: 1,
        explanation: "A palavra-chave `lambda` define funções anônimas (ex: `quadrado = lambda x: x ** 2`)."
      }
    ]
  },
  {
    id: "mod-07",
    title: "Módulo 07: Programação Orientada a Objetos (POO)",
    questions: [
      {
        question: "Qual é o método especial construtor/inicializador de uma classe em Python?",
        options: ["__construct__", "__init__", "__new__", "__create__"],
        answer: 1,
        explanation: "`__init__(self, ...)` é o método chamado automaticamente após a criação da instância para inicializar seus atributos."
      },
      {
        question: "O que representa o primeiro parâmetro `self` nos métodos de instância?",
        options: [
          "A própria classe",
          "A referência explícita à instância atual do objeto",
          "Uma palavra reservada obrigatória do interpretador",
          "O escopo global"
        ],
        answer: 1,
        explanation: "`self` referencia a instância atual na qual o método está sendo executado."
      }
    ]
  }
];

// Cheat sheet data
const CHEATSHEET_DATA = {
  basics: [
    { title: "Comentários", code: "# Linha única\n'''\nMúltiplas linhas\nou docstrings\n'''" },
    { title: "Entrada e Saída", code: "print('Olá, Mundo!', end='\\n')\nnome = input('Digite seu nome: ')\nprint(f'Bem-vindo, {nome}!')" },
    { title: "Tipos Básicos", code: "idade = 25          # int\naltura = 1.75       # float\nnome = 'Alex'       # str\nativo = True        # bool\nnulo = None         # NoneType" }
  ],
  collections: [
    { title: "Listas (list)", code: "frutas = ['maçã', 'banana', 'laranja']\nfrutas.append('uva')\nfrutas.insert(1, 'manga')\nfrutas.pop()           # Remove último\nfrutas.remove('banana')\nprint(frutas[0:2])     # Fatiamento (Slicing)" },
    { title: "Dicionários (dict)", code: "aluno = {'nome': 'Carlos', 'nota': 9.5}\naluno['curso'] = 'Python'\nvalor = aluno.get('idade', 18)\nfor k, v in aluno.items():\n    print(f'{k}: {v}')" },
    { title: "Tuplas & Conjuntos", code: "coordenadas = (10, 20)      # Tupla (imutável)\nunicos = {1, 2, 2, 3}          # Set: {1, 2, 3}\nunicos.add(4)" },
    { title: "List Comprehension", code: "# [expressão for item in iterável if condição]\npares_quadrados = [x**2 for x in range(10) if x % 2 == 0]\n# [0, 4, 16, 36, 64]" }
  ],
  control_flow: [
    { title: "Condicionais (if/elif/else)", code: "if nota >= 9.0:\n    print('Excelente')\nelif nota >= 7.0:\n    print('Aprovado')\nelse:\n    print('Recuperação')\n\n# Operador Ternário\nstatus = 'Maior' if idade >= 18 else 'Menor'" },
    { title: "Loops (for & while)", code: "for i in range(1, 6):\n    if i == 3: continue\n    print(i)\n\ncontador = 0\nwhile contador < 5:\n    print(contador)\n    contador += 1" },
    { title: "Tratamento de Exceções", code: "try:\n    resultado = 10 / divisor\nexcept ZeroDivisionError as e:\n    print('Divisão por zero proibida!')\nexcept Exception as err:\n    print(f'Erro inesperado: {err}')\nelse:\n    print('Sucesso:', resultado)\nfinally:\n    print('Executado sempre')" }
  ],
  functions_oop: [
    { title: "Funções & Lambdas", code: "def somar(a: int, b: int = 10) -> int:\n    '''Retorna a soma de a e b.'''\n    return a + b\n\n# Lambda\ndobro = lambda x: x * 2" },
    { title: "Args & Kwargs", code: "def relatorio(*args, **kwargs):\n    for item in args: print(item)\n    for k, v in kwargs.items(): print(f'{k}={v}')\n\nrelatorio(1, 2, 3, status='ok', ver='3.12')" },
    { title: "Classes & Objetos", code: "class Programador:\n    def __init__(self, nome, linguagem):\n        self.nome = nome\n        self.linguagem = linguagem\n    \n    def codificar(self):\n        return f'{self.nome} codificando em {self.linguagem}!'\n\ndev = Programador('Ana', 'Python')\nprint(dev.codificar())" }
  ]
};

// Python snippets for Sandbox
const PYTHON_SNIPPETS = [
  {
    name: "01. Olá Mundo & Interatividade",
    code: `# Bem-vindo ao Sandbox Python Integrado!
# Pressione Executar (ou Ctrl+Enter) para rodar o código instantaneamente no navegador.

import sys
import datetime

nome = "Estudante"
hora_atual = datetime.datetime.now().strftime("%H:%M:%S")

print("=" * 45)
print(f"  🐍 Meus Estudos Hub - Python {sys.version.split()[0]}")
print("=" * 45)
print(f"Olá, {nome}! Sessão iniciada às {hora_atual}.")
print("Pronto para praticar lógica, algoritmos e estruturas de dados!")
`
  },
  {
    name: "02. List Comprehensions & Manipulação de Dados",
    code: `# List Comprehensions, Filtros e Estatísticas

numeros = [12, 45, 7, 23, 56, 89, 34, 2, 78, 91, 100]

pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]
quadrados_pares = [n**2 for n in pares]

print(f"Lista original: {numeros}")
print(f"Números pares ({len(pares)}): {pares}")
print(f"Números ímpares ({len(impares)}): {impares}")
print(f"Quadrado dos pares: {quadrados_pares}")
print(f"Soma total: {sum(numeros)} | Média: {sum(numeros)/len(numeros):.2f}")
print(f"Mínimo: {min(numeros)} | Máximo: {max(numeros)}")
`
  },
  {
    name: "03. Algoritmo Bubble Sort Passo a Passo",
    code: `# Algoritmo de Ordenação: Bubble Sort
def bubble_sort(lista):
    n = len(lista)
    passos = 0
    arr = lista.copy()
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            passos += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocou = True
        if not trocou:
            break
    return arr, passos

desordenada = [64, 34, 25, 12, 22, 11, 90, 5, 42]
ordenada, comparacoes = bubble_sort(desordenada)

print(f"Original : {desordenada}")
print(f"Ordenada : {ordenada}")
print(f"Total de comparações realizadas: {comparacoes}")
`
  },
  {
    name: "04. Dicionários e Agrupamento",
    code: `# Estrutura de Dicionários e Agrupamento de Dados

estudantes = [
    {"nome": "Marina", "curso": "Python", "nota": 9.8},
    {"nome": "Lucas", "curso": "JavaScript", "nota": 8.5},
    {"nome": "Beatriz", "curso": "Python", "nota": 9.2},
    {"nome": "Rafael", "curso": "Python", "nota": 7.4},
    {"nome": "Camila", "curso": "JavaScript", "nota": 9.0},
]

# Agrupamento por curso
por_curso = {}
for est in estudantes:
    curso = est["curso"]
    if curso not in por_curso:
        por_curso[curso] = []
    por_curso[curso].append(est)

print("--- RELATÓRIO DE DESEMPENHO ---")
for curso, lista in por_curso.items():
    media = sum(e["nota"] for e in lista) / len(lista)
    print(f"\n📘 Curso: {curso} (Total: {len(lista)} alunos, Média: {media:.2f})")
    for e in lista:
        badge = "⭐ Destaque" if e["nota"] >= 9.0 else "✅ Regular"
        print(f"  • {e['nome']:<10} - Nota: {e['nota']} ({badge})")
`
  },
  {
    name: "05. POO: Herança e Polimorfismo",
    code: `# Programação Orientada a Objetos

class ContaBancaria:
    def __init__(self, titular: str, saldo: float = 0.0):
        self.titular = titular
        self._saldo = saldo
    
    def depositar(self, valor: float):
        if valor > 0:
            self._saldo += valor
            print(f"[+] Depósito de R$ {valor:.2f} realizado.")
        else:
            print("[!] Valor de depósito inválido.")
            
    def sacar(self, valor: float) -> bool:
        if 0 < valor <= self._saldo:
            self._saldo -= valor
            print(f"[-] Saque de R$ {valor:.2f} realizado.")
            return True
        print("[!] Saldo insuficiente ou valor inválido.")
        return False
        
    def extrato(self):
        return f"Conta de {self.titular} | Saldo Atual: R$ {self._saldo:.2f}"

class ContaPoupanca(ContaBancaria):
    def render_juros(self, taxa_percentual: float = 0.5):
        rendimento = self._saldo * (taxa_percentual / 100)
        self._saldo += rendimento
        print(f"[📈] Juros de R$ {rendimento:.2f} aplicados.")

c1 = ContaPoupanca("Alex Silva", 1500.0)
print(c1.extrato())
c1.depositar(500)
c1.render_juros(1.2)
c1.sacar(300)
print(c1.extrato())
`
  }
];

function generateAppHtml(tree, allFilesList) {
  const treeJson = JSON.stringify(tree);
  const filesJson = JSON.stringify(allFilesList);
  const quizzesJson = JSON.stringify(QUIZZES_DATA);
  const cheatsheetJson = JSON.stringify(CHEATSHEET_DATA);
  const snippetsJson = JSON.stringify(PYTHON_SNIPPETS);

  return `<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Meus Estudos - Hub Interativo de Aprendizado</title>
  <meta name="description" content="Plataforma interativa para estudo e revisão de Python, JavaScript, Jupyter Notebooks, apostilas e exercícios práticos com Sandbox Pyodide embutido.">
  
  <!-- Google Fonts & Font Awesome -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Outfit:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  
  <!-- Highlight.js & Marked for in-browser rendering -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/tokyo-night-dark.min.css">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/python.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/javascript.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/markdown.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  
  <!-- Pyodide for In-Browser Python 3 Runner -->
  <script src="https://cdn.jsdelivr.net/pyodide/v0.25.1/full/pyodide.js"></script>

  <style>
    :root {
      --bg-base: #090d16;
      --bg-surface: #0f172a;
      --bg-card: rgba(19, 29, 51, 0.7);
      --bg-card-hover: rgba(30, 45, 77, 0.85);
      --glass-border: rgba(255, 255, 255, 0.08);
      --glass-border-hover: rgba(56, 189, 248, 0.4);
      --primary: #38bdf8;
      --primary-rgb: 56, 189, 248;
      --primary-glow: rgba(56, 189, 248, 0.35);
      --secondary: #818cf8;
      --accent-green: #34d399;
      --accent-yellow: #fbbf24;
      --accent-red: #f87171;
      --accent-purple: #c084fc;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
      --font-code: 'Fira Code', monospace;
      --transition-smooth: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif; }
    
    body {
      background-color: var(--bg-base);
      background-image: 
        radial-gradient(at 0% 0%, rgba(56, 189, 248, 0.12) 0px, transparent 50%),
        radial-gradient(at 100% 0%, rgba(129, 140, 248, 0.12) 0px, transparent 50%),
        radial-gradient(at 50% 100%, rgba(52, 211, 153, 0.08) 0px, transparent 50%);
      background-attachment: fixed;
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      overflow-x: hidden;
    }

    /* Scrollbars */
    ::-webkit-scrollbar { width: 8px; height: 8px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.15); border-radius: 99px; }
    ::-webkit-scrollbar-thumb:hover { background: rgba(56, 189, 248, 0.4); }

    /* Top Navigation Header */
    header {
      padding: 0.9rem 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--glass-border);
      position: sticky;
      top: 0;
      z-index: 50;
      gap: 1.5rem;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 0.85rem;
      text-decoration: none;
      color: inherit;
      cursor: pointer;
    }

    .brand-logo-badge {
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: linear-gradient(135deg, rgba(56, 189, 248, 0.25), rgba(129, 140, 248, 0.25));
      border: 1px solid rgba(56, 189, 248, 0.4);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--primary);
      font-size: 1.35rem;
      box-shadow: 0 0 15px var(--primary-glow);
      transition: var(--transition-smooth);
    }
    .brand:hover .brand-logo-badge {
      transform: rotate(-5deg) scale(1.05);
      box-shadow: 0 0 25px var(--primary-glow);
    }

    .brand-info h1 {
      font-size: 1.3rem;
      font-weight: 700;
      letter-spacing: -0.5px;
      background: linear-gradient(135deg, #ffffff, #38bdf8);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .brand-info span {
      font-size: 0.75rem;
      color: var(--text-muted);
      font-weight: 500;
      display: block;
    }

    /* Universal Search Bar */
    .search-wrapper {
      position: relative;
      flex: 1;
      max-width: 440px;
    }
    .search-wrapper input {
      width: 100%;
      background: rgba(9, 13, 22, 0.6);
      border: 1px solid var(--glass-border);
      border-radius: 99px;
      padding: 0.65rem 3rem 0.65rem 2.8rem;
      color: var(--text-main);
      font-size: 0.95rem;
      outline: none;
      transition: var(--transition-smooth);
    }
    .search-wrapper input:focus {
      border-color: var(--primary);
      background: rgba(15, 23, 42, 0.9);
      box-shadow: 0 0 20px var(--primary-glow);
    }
    .search-wrapper .search-icon {
      position: absolute;
      left: 1.1rem;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-dim);
      font-size: 0.9rem;
      pointer-events: none;
    }
    .search-wrapper .search-shortcut {
      position: absolute;
      right: 1rem;
      top: 50%;
      transform: translateY(-50%);
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid var(--glass-border);
      padding: 0.15rem 0.45rem;
      border-radius: 6px;
      font-size: 0.7rem;
      color: var(--text-muted);
      font-family: var(--font-code);
      pointer-events: none;
    }

    /* Header Action Buttons */
    .header-actions {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .btn-action {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid var(--glass-border);
      color: var(--text-main);
      padding: 0.55rem 1rem;
      border-radius: var(--radius-sm);
      font-size: 0.88rem;
      font-weight: 500;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      transition: var(--transition-smooth);
      white-space: nowrap;
    }
    .btn-action:hover {
      background: rgba(56, 189, 248, 0.15);
      border-color: var(--primary);
      color: var(--primary);
      transform: translateY(-1px);
    }
    .btn-action.active {
      background: var(--primary);
      color: #090d16;
      font-weight: 600;
      border-color: var(--primary);
    }

    /* Pomodoro Header Widget */
    .pomodoro-widget {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      background: rgba(15, 23, 42, 0.9);
      border: 1px solid rgba(248, 113, 113, 0.3);
      padding: 0.4rem 0.85rem;
      border-radius: 99px;
      font-family: var(--font-code);
      font-size: 0.9rem;
      color: #fca5a5;
    }
    .pomodoro-widget .pomo-btn {
      background: transparent;
      border: none;
      color: inherit;
      cursor: pointer;
      font-size: 0.9rem;
      padding: 0.2rem;
      transition: 0.2s;
    }
    .pomodoro-widget .pomo-btn:hover { color: #ffffff; transform: scale(1.15); }
    .pomodoro-time { font-weight: 600; letter-spacing: 0.5px; }

    /* XP & Level Badge */
    .user-stats-badge {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      background: linear-gradient(135deg, rgba(251, 191, 36, 0.15), rgba(129, 140, 248, 0.15));
      border: 1px solid rgba(251, 191, 36, 0.3);
      padding: 0.45rem 0.9rem;
      border-radius: 99px;
      font-size: 0.85rem;
      color: #fef08a;
      font-weight: 600;
    }

    /* Main Workspace Layout */
    .workspace-layout {
      display: flex;
      flex: 1;
      height: calc(100vh - 72px);
      overflow: hidden;
    }

    /* Sidebar */
    aside.sidebar {
      width: 290px;
      min-width: 290px;
      background: rgba(15, 23, 42, 0.6);
      border-right: 1px solid var(--glass-border);
      backdrop-filter: blur(12px);
      display: flex;
      flex-direction: column;
      padding: 1.25rem 1rem;
      overflow-y: auto;
      gap: 1.5rem;
    }

    .sidebar-section-title {
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: var(--text-dim);
      margin-bottom: 0.5rem;
      padding-left: 0.5rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .nav-group {
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
    }

    .nav-btn {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.65rem 0.85rem;
      border-radius: var(--radius-sm);
      background: transparent;
      border: 1px solid transparent;
      color: var(--text-muted);
      cursor: pointer;
      font-size: 0.9rem;
      font-weight: 500;
      transition: var(--transition-smooth);
      text-align: left;
      width: 100%;
    }
    .nav-btn .nav-left {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }
    .nav-btn i { font-size: 1rem; width: 18px; text-align: center; }
    .nav-btn .badge-count {
      font-size: 0.75rem;
      padding: 0.15rem 0.5rem;
      border-radius: 99px;
      background: rgba(255, 255, 255, 0.05);
      color: var(--text-dim);
    }
    .nav-btn:hover {
      background: rgba(255, 255, 255, 0.04);
      color: var(--text-main);
      transform: translateX(3px);
    }
    .nav-btn.active {
      background: rgba(56, 189, 248, 0.12);
      border-color: rgba(56, 189, 248, 0.3);
      color: var(--primary);
      font-weight: 600;
    }
    .nav-btn.active .badge-count {
      background: rgba(56, 189, 248, 0.2);
      color: var(--primary);
    }

    /* Study Progress Card in Sidebar */
    .study-progress-card {
      background: rgba(19, 29, 51, 0.5);
      border: 1px solid var(--glass-border);
      border-radius: var(--radius-md);
      padding: 1rem;
      margin-top: auto;
    }
    .progress-header {
      display: flex;
      justify-content: space-between;
      font-size: 0.82rem;
      color: var(--text-muted);
      margin-bottom: 0.5rem;
      font-weight: 600;
    }
    .progress-bar-bg {
      width: 100%;
      height: 8px;
      border-radius: 99px;
      background: rgba(255, 255, 255, 0.08);
      overflow: hidden;
      position: relative;
    }
    .progress-bar-fill {
      height: 100%;
      border-radius: 99px;
      background: linear-gradient(90deg, #38bdf8, #34d399);
      width: 0%;
      transition: width 0.6s ease;
    }
    .progress-subtext {
      display: flex;
      justify-content: space-between;
      font-size: 0.75rem;
      color: var(--text-dim);
      margin-top: 0.5rem;
    }

    /* Main Content Area */
    main.main-content {
      flex: 1;
      display: flex;
      flex-direction: column;
      overflow-y: auto;
      padding: 1.5rem 2rem;
      gap: 1.5rem;
    }

    /* Controls Bar: Breadcrumbs, View Toggle, Sort */
    .controls-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 1rem;
    }

    .breadcrumbs {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.95rem;
      color: var(--text-muted);
      flex-wrap: wrap;
    }
    .breadcrumbs span {
      cursor: pointer;
      transition: 0.2s;
    }
    .breadcrumbs span:hover { color: var(--primary); }
    .breadcrumbs .current {
      color: var(--text-main);
      font-weight: 600;
      cursor: default;
    }
    .breadcrumbs i { font-size: 0.75rem; color: var(--text-dim); }

    .view-filter-controls {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .filter-pills {
      display: flex;
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid var(--glass-border);
      border-radius: 99px;
      padding: 0.25rem;
      gap: 0.2rem;
    }
    .filter-pill {
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-size: 0.8rem;
      padding: 0.35rem 0.8rem;
      border-radius: 99px;
      cursor: pointer;
      transition: 0.2s;
      font-weight: 500;
    }
    .filter-pill:hover { color: var(--text-main); }
    .filter-pill.active {
      background: rgba(56, 189, 248, 0.2);
      color: var(--primary);
      font-weight: 600;
    }

    .view-toggle {
      display: flex;
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid var(--glass-border);
      border-radius: var(--radius-sm);
      overflow: hidden;
    }
    .view-toggle-btn {
      background: transparent;
      border: none;
      color: var(--text-muted);
      padding: 0.45rem 0.75rem;
      cursor: pointer;
      font-size: 0.85rem;
      transition: 0.2s;
    }
    .view-toggle-btn.active {
      background: rgba(56, 189, 248, 0.2);
      color: var(--primary);
    }

    /* Grid of Files */
    .study-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
      gap: 1.25rem;
    }

    .study-card {
      background: var(--bg-card);
      border: 1px solid var(--glass-border);
      border-radius: var(--radius-md);
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
      cursor: pointer;
      position: relative;
      transition: var(--transition-smooth);
      backdrop-filter: blur(8px);
      text-decoration: none;
      color: inherit;
    }
    .study-card:hover {
      transform: translateY(-4px);
      background: var(--bg-card-hover);
      border-color: var(--glass-border-hover);
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4), 0 0 20px rgba(56, 189, 248, 0.1);
    }

    .card-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
    }

    .card-icon-badge {
      width: 48px;
      height: 48px;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.6rem;
      transition: transform 0.3s;
    }
    .study-card:hover .card-icon-badge {
      transform: scale(1.1) rotate(-3deg);
    }

    /* Icon badge styles */
    .badge-folder { background: rgba(234, 179, 8, 0.15); color: #fbbf24; }
    .badge-py { background: rgba(59, 130, 246, 0.15); color: #60a5fa; }
    .badge-ipynb { background: rgba(249, 115, 22, 0.15); color: #fb923c; }
    .badge-md { background: rgba(168, 85, 247, 0.15); color: #c084fc; }
    .badge-pdf { background: rgba(236, 72, 153, 0.15); color: #f472b6; }
    .badge-html { background: rgba(239, 68, 68, 0.15); color: #f87171; }
    .badge-generic { background: rgba(148, 163, 184, 0.15); color: #94a3b8; }

    .card-quick-actions {
      display: flex;
      gap: 0.35rem;
    }
    .card-action-btn {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid transparent;
      color: var(--text-dim);
      width: 32px;
      height: 32px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.85rem;
      cursor: pointer;
      transition: 0.2s;
    }
    .card-action-btn:hover {
      background: rgba(56, 189, 248, 0.2);
      color: var(--primary);
    }
    .card-action-btn.starred {
      color: #fbbf24;
    }
    .card-action-btn.completed {
      color: #34d399;
    }

    .card-body {
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
    }
    .card-title {
      font-size: 1rem;
      font-weight: 600;
      color: var(--text-main);
      word-break: break-word;
      line-height: 1.4;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }
    .card-category {
      font-size: 0.75rem;
      color: var(--text-dim);
      font-weight: 500;
    }

    .card-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px solid rgba(255, 255, 255, 0.05);
      padding-top: 0.65rem;
      font-size: 0.75rem;
      color: var(--text-muted);
    }

    .card-tag {
      background: rgba(255, 255, 255, 0.06);
      padding: 0.15rem 0.5rem;
      border-radius: 6px;
      font-family: var(--font-code);
      font-size: 0.7rem;
    }

    /* List View Table */
    .study-table-container {
      background: var(--bg-card);
      border: 1px solid var(--glass-border);
      border-radius: var(--radius-md);
      overflow-x: auto;
    }
    .study-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.9rem;
    }
    .study-table th {
      background: rgba(15, 23, 42, 0.8);
      padding: 0.85rem 1.25rem;
      font-weight: 600;
      color: var(--text-muted);
      border-bottom: 1px solid var(--glass-border);
    }
    .study-table td {
      padding: 0.85rem 1.25rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.03);
      color: var(--text-main);
    }
    .study-table tr:hover td {
      background: rgba(56, 189, 248, 0.05);
      cursor: pointer;
    }

    /* Empty State */
    .empty-state {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      padding: 5rem 2rem;
      text-align: center;
      gap: 1rem;
      color: var(--text-muted);
    }
    .empty-state i { font-size: 4rem; opacity: 0.3; color: var(--primary); }
    .empty-state h3 { font-size: 1.4rem; color: var(--text-main); }

    /* Modals System (Reader, Sandbox, Quizzes, Notes, CheatSheet) */
    .modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(9, 13, 22, 0.85);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      z-index: 1000;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.25s ease;
    }
    .modal-overlay.active {
      opacity: 1;
      pointer-events: auto;
    }

    .modal-window {
      background: var(--bg-surface);
      border: 1px solid var(--glass-border);
      border-radius: var(--radius-lg);
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.6);
      width: 100%;
      max-width: 1100px;
      height: 90vh;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      transform: scale(0.96);
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .modal-overlay.active .modal-window {
      transform: scale(1);
    }

    .modal-header {
      padding: 1rem 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--glass-border);
      background: rgba(15, 23, 42, 0.8);
    }
    .modal-title {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      font-size: 1.15rem;
      font-weight: 600;
    }
    .modal-title i { color: var(--primary); }
    .modal-close-btn {
      background: rgba(255, 255, 255, 0.06);
      border: none;
      color: var(--text-muted);
      width: 34px;
      height: 34px;
      border-radius: 8px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.1rem;
      transition: 0.2s;
    }
    .modal-close-btn:hover { background: rgba(248, 113, 113, 0.2); color: #f87171; }

    .modal-body {
      flex: 1;
      overflow-y: auto;
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    /* Embedded Reader Content Styles */
    .reader-container {
      font-size: 1rem;
      line-height: 1.7;
      color: #cbd5e1;
    }
    .reader-container h1, .reader-container h2, .reader-container h3 {
      color: #f8fafc;
      margin: 1.25rem 0 0.75rem 0;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      padding-bottom: 0.4rem;
    }
    .reader-container code {
      font-family: var(--font-code);
      background: rgba(0,0,0,0.3);
      padding: 0.2rem 0.4rem;
      border-radius: 4px;
      color: #fde047;
      font-size: 0.9em;
    }
    .reader-container pre {
      background: #0d1117;
      border: 1px solid var(--glass-border);
      border-radius: var(--radius-sm);
      padding: 1rem;
      overflow-x: auto;
      margin: 1rem 0;
      position: relative;
    }
    .reader-container pre code {
      background: transparent;
      padding: 0;
      color: inherit;
    }

    .nb-cell { margin-bottom: 1.5rem; }
    .nb-cell-code {
      background: #0d1117;
      border: 1px solid var(--glass-border);
      border-radius: var(--radius-sm);
      padding: 1rem;
      position: relative;
    }
    .nb-cell-output {
      background: #06090e;
      border-left: 3px solid var(--accent-green);
      color: #86efac;
      padding: 0.85rem 1rem;
      border-radius: 0 0 var(--radius-sm) var(--radius-sm);
      font-family: var(--font-code);
      font-size: 0.88rem;
      white-space: pre-wrap;
      overflow-x: auto;
      margin-top: 0.25rem;
    }
    .btn-run-cell {
      position: absolute;
      top: 0.6rem;
      right: 0.6rem;
      background: rgba(56, 189, 248, 0.15);
      border: 1px solid rgba(56, 189, 248, 0.3);
      color: var(--primary);
      padding: 0.25rem 0.6rem;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.35rem;
      transition: 0.2s;
    }
    .btn-run-cell:hover {
      background: var(--primary);
      color: #090d16;
    }

    /* Sandbox Styles */
    .sandbox-layout {
      display: grid;
      grid-template-columns: 1.2fr 1fr;
      gap: 1.25rem;
      height: 100%;
    }
    @media (max-width: 850px) {
      .sandbox-layout { grid-template-columns: 1fr; }
    }

    .sandbox-editor-panel, .sandbox-output-panel {
      display: flex;
      flex-direction: column;
      background: #0b1120;
      border: 1px solid var(--glass-border);
      border-radius: var(--radius-md);
      overflow: hidden;
    }

    .panel-toolbar {
      padding: 0.6rem 1rem;
      background: rgba(15, 23, 42, 0.9);
      border-bottom: 1px solid var(--glass-border);
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.85rem;
    }

    .sandbox-textarea {
      flex: 1;
      width: 100%;
      background: #080c14;
      color: #f8fafc;
      font-family: var(--font-code);
      font-size: 0.95rem;
      line-height: 1.5;
      padding: 1rem;
      border: none;
      outline: none;
      resize: none;
      tab-size: 4;
    }

    .sandbox-terminal {
      flex: 1;
      background: #05080f;
      padding: 1rem;
      font-family: var(--font-code);
      font-size: 0.88rem;
      line-height: 1.6;
      color: #38bdf8;
      overflow-y: auto;
      white-space: pre-wrap;
      word-break: break-word;
    }
    .sandbox-terminal .term-error { color: #f87171; }
    .sandbox-terminal .term-success { color: #34d399; }
    .sandbox-terminal .term-system { color: #94a3b8; font-style: italic; }

    /* Quiz Panel Styles */
    .quiz-card {
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid var(--glass-border);
      border-radius: var(--radius-md);
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }
    .quiz-question-text {
      font-size: 1.1rem;
      font-weight: 600;
      color: #f8fafc;
    }
    .quiz-options {
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
    }
    .quiz-option-btn {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid var(--glass-border);
      border-radius: var(--radius-sm);
      padding: 0.85rem 1rem;
      color: var(--text-main);
      text-align: left;
      font-size: 0.95rem;
      cursor: pointer;
      transition: var(--transition-smooth);
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }
    .quiz-option-btn:hover {
      background: rgba(56, 189, 248, 0.1);
      border-color: var(--primary);
    }
    .quiz-option-btn.correct {
      background: rgba(52, 211, 153, 0.2) !important;
      border-color: #34d399 !important;
      color: #6ee7b7 !important;
    }
    .quiz-option-btn.incorrect {
      background: rgba(248, 113, 113, 0.2) !important;
      border-color: #f87171 !important;
      color: #fca5a5 !important;
    }
    .quiz-explanation {
      background: rgba(30, 41, 59, 0.6);
      border-left: 3px solid var(--primary);
      padding: 0.75rem 1rem;
      border-radius: 0 8px 8px 0;
      font-size: 0.9rem;
      color: var(--text-muted);
    }

    /* Cheat Sheet Tabs */
    .tabs-nav {
      display: flex;
      gap: 0.5rem;
      border-bottom: 1px solid var(--glass-border);
      padding-bottom: 0.75rem;
      overflow-x: auto;
    }
    .tab-btn {
      background: transparent;
      border: none;
      color: var(--text-muted);
      padding: 0.5rem 1rem;
      border-radius: var(--radius-sm);
      cursor: pointer;
      font-size: 0.9rem;
      font-weight: 500;
      transition: 0.2s;
    }
    .tab-btn:hover { color: var(--text-main); }
    .tab-btn.active {
      background: rgba(56, 189, 248, 0.15);
      color: var(--primary);
      font-weight: 600;
    }

    .cheatsheet-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 1.25rem;
    }
    .cheatsheet-card {
      background: rgba(15, 23, 42, 0.6);
      border: 1px solid var(--glass-border);
      border-radius: var(--radius-md);
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }
    .cheatsheet-card h4 {
      color: var(--primary);
      font-size: 0.95rem;
    }

    /* Notes Area */
    .notes-textarea {
      width: 100%;
      height: 400px;
      background: #080c14;
      border: 1px solid var(--glass-border);
      border-radius: var(--radius-md);
      color: #f8fafc;
      padding: 1rem;
      font-family: var(--font-code);
      font-size: 0.95rem;
      line-height: 1.6;
      outline: none;
      resize: vertical;
    }

    /* Responsive */
    @media (max-width: 900px) {
      aside.sidebar { display: none; }
      header { padding: 0.75rem 1rem; }
      .search-wrapper { max-width: 250px; }
      main.main-content { padding: 1rem; }
    }
  </style>
</head>
<body>

  <!-- Top Header Navigation -->
  <header>
    <div class="brand" onclick="navigateToRoot()">
      <div class="brand-logo-badge">
        <i class="fa-solid fa-graduation-cap"></i>
      </div>
      <div class="brand-info">
        <h1>Meus Estudos</h1>
        <span>Portal Interativo & Playground</span>
      </div>
    </div>

    <div class="search-wrapper">
      <i class="fa-solid fa-magnifying-glass search-icon"></i>
      <input type="text" id="globalSearch" placeholder="Buscar 500+ aulas, notebooks, códigos..." autocomplete="off">
      <span class="search-shortcut">Ctrl+K</span>
    </div>

    <div class="header-actions">
      <!-- Pomodoro Timer Widget -->
      <div class="pomodoro-widget" title="Timer Pomodoro (25m Foco / 5m Pausa)">
        <i class="fa-solid fa-stopwatch" style="color: #f87171;"></i>
        <span class="pomodoro-time" id="pomoTime">25:00</span>
        <button class="pomo-btn" id="pomoToggleBtn" onclick="togglePomodoro()"><i class="fa-solid fa-play"></i></button>
        <button class="pomo-btn" onclick="resetPomodoro()"><i class="fa-solid fa-rotate-right"></i></button>
      </div>

      <!-- Quick Modals Triggers -->
      <button class="btn-action" onclick="openSandboxModal()" title="Abrir Python Sandbox Interativo (Alt+S)">
        <i class="fa-brands fa-python" style="color: #38bdf8;"></i>
        <span>Sandbox</span>
      </button>

      <button class="btn-action" onclick="openQuizzesModal()" title="Bateria de Quizzes e Desafios">
        <i class="fa-solid fa-brain" style="color: #fbbf24;"></i>
        <span>Quizzes</span>
      </button>

      <button class="btn-action" onclick="openCheatSheetModal()" title="Guia Rápido de Referência">
        <i class="fa-solid fa-bolt" style="color: #c084fc;"></i>
        <span>Cheat Sheet</span>
      </button>

      <button class="btn-action" onclick="openNotesModal()" title="Minhas Anotações de Estudo">
        <i class="fa-solid fa-pen-to-square" style="color: #34d399;"></i>
        <span>Notas</span>
      </button>

      <!-- XP Stats -->
      <div class="user-stats-badge" id="xpBadge" title="Nível de Aprendizado e XP Total">
        <i class="fa-solid fa-fire" style="color: #fbbf24;"></i>
        <span id="userLevelText">Nível 1</span>
        <span id="userXpText" style="opacity: 0.8; font-size: 0.75rem;">(0 XP)</span>
      </div>
    </div>
  </header>

  <!-- Workspace Layout -->
  <div class="workspace-layout">
    <!-- Sidebar Navigation -->
    <aside class="sidebar">
      <div>
        <div class="sidebar-section-title"><i class="fa-solid fa-compass"></i> Navegação Rápida</div>
        <div class="nav-group">
          <button class="nav-btn active" id="navAll" onclick="filterByNav('all')">
            <span class="nav-left"><i class="fa-solid fa-layer-group" style="color: #38bdf8;"></i> Todos os Arquivos</span>
            <span class="badge-count" id="countAll">0</span>
          </button>
          <button class="nav-btn" id="navStarred" onclick="filterByNav('starred')">
            <span class="nav-left"><i class="fa-solid fa-star" style="color: #fbbf24;"></i> Favoritos</span>
            <span class="badge-count" id="countStarred">0</span>
          </button>
          <button class="nav-btn" id="navCompleted" onclick="filterByNav('completed')">
            <span class="nav-left"><i class="fa-solid fa-circle-check" style="color: #34d399;"></i> Concluídos</span>
            <span class="badge-count" id="countCompleted">0</span>
          </button>
        </div>
      </div>

      <div>
        <div class="sidebar-section-title"><i class="fa-solid fa-graduation-cap"></i> Trilhas de Estudo</div>
        <div class="nav-group" id="categoryNavList">
          <!-- Injected via JS -->
        </div>
      </div>

      <!-- Study Progress Box -->
      <div class="study-progress-card">
        <div class="progress-header">
          <span><i class="fa-solid fa-chart-line"></i> Progresso Geral</span>
          <span id="progressPercent">0%</span>
        </div>
        <div class="progress-bar-bg">
          <div class="progress-bar-fill" id="progressBarFill"></div>
        </div>
        <div class="progress-subtext">
          <span id="progressCompletedText">0 / 0 concluídos</span>
          <span id="streakText">🔥 1 dia</span>
        </div>
      </div>
    </aside>

    <!-- Main Content Explorer -->
    <main class="main-content">
      <!-- Controls Bar -->
      <div class="controls-bar">
        <div class="breadcrumbs" id="breadcrumbs">
          <span onclick="navigateToRoot()"><i class="fa-solid fa-house"></i> Início</span>
          <i class="fa-solid fa-chevron-right"></i>
          <span class="current" id="currentBreadcrumb">Todos os Conteúdos</span>
        </div>

        <div class="view-filter-controls">
          <!-- Type Filter Pills -->
          <div class="filter-pills">
            <button class="filter-pill active" onclick="setTypeFilter('all', this)">Todos</button>
            <button class="filter-pill" onclick="setTypeFilter('.ipynb', this)">Notebooks</button>
            <button class="filter-pill" onclick="setTypeFilter('.py', this)">Python</button>
            <button class="filter-pill" onclick="setTypeFilter('.md', this)">Markdown</button>
            <button class="filter-pill" onclick="setTypeFilter('.pdf', this)">PDFs</button>
          </div>

          <!-- View Toggle (Grid / List) -->
          <div class="view-toggle">
            <button class="view-toggle-btn active" id="btnViewGrid" onclick="setViewMode('grid')" title="Visualização em Grade"><i class="fa-solid fa-grip"></i></button>
            <button class="view-toggle-btn" id="btnViewList" onclick="setViewMode('list')" title="Visualização em Lista"><i class="fa-solid fa-list"></i></button>
          </div>
        </div>
      </div>

      <!-- File Cards / Table View Container -->
      <div id="contentContainer">
        <!-- Injected via JS -->
      </div>
    </main>
  </div>

  <!-- MODAL: Leitor Integrado (Notebooks, MD, Python, PDF) -->
  <div class="modal-overlay" id="readerModal">
    <div class="modal-window">
      <div class="modal-header">
        <div class="modal-title">
          <i id="readerFileIcon" class="fa-solid fa-file-code"></i>
          <span id="readerFileName">Visualizador de Aula</span>
        </div>
        <div style="display: flex; gap: 0.6rem; align-items: center;">
          <button class="btn-action" id="readerToggleCompleteBtn" onclick="toggleCurrentFileComplete()">
            <i class="fa-regular fa-circle-check"></i> Marcar Concluído
          </button>
          <button class="btn-action" id="readerOpenSandboxBtn" style="display:none;" onclick="openCurrentInSandbox()">
            <i class="fa-brands fa-python"></i> Testar no Sandbox
          </button>
          <a id="readerExternalLink" href="#" target="_blank" class="btn-action" title="Abrir em Nova Aba">
            <i class="fa-solid fa-arrow-up-right-from-square"></i>
          </a>
          <button class="modal-close-btn" onclick="closeModal('readerModal')"><i class="fa-solid fa-xmark"></i></button>
        </div>
      </div>
      <div class="modal-body" id="readerModalBody">
        <!-- Injected dynamically -->
      </div>
    </div>
  </div>

  <!-- MODAL: Python Sandbox (Pyodide) -->
  <div class="modal-overlay" id="sandboxModal">
    <div class="modal-window">
      <div class="modal-header">
        <div class="modal-title">
          <i class="fa-brands fa-python" style="color: #38bdf8;"></i>
          <span>Sandbox Python 3 (Pyodide WebAssembly)</span>
        </div>
        <div style="display: flex; gap: 0.6rem; align-items: center;">
          <select id="snippetSelect" onchange="loadSnippet(this.value)" class="btn-action" style="background:#0f172a; outline:none;">
            <option value="">💡 Carregar Exemplo / Snippet...</option>
          </select>
          <button class="btn-action active" onclick="runSandboxCode()"><i class="fa-solid fa-play"></i> Executar (Ctrl+Enter)</button>
          <button class="btn-action" onclick="clearTerminal()"><i class="fa-solid fa-trash-can"></i> Limpar</button>
          <button class="modal-close-btn" onclick="closeModal('sandboxModal')"><i class="fa-solid fa-xmark"></i></button>
        </div>
      </div>
      <div class="modal-body" style="padding: 1rem;">
        <div class="sandbox-layout">
          <div class="sandbox-editor-panel">
            <div class="panel-toolbar">
              <span><i class="fa-solid fa-code"></i> Editor de Código</span>
              <span style="font-size: 0.75rem; color: var(--text-dim);">Tab suportado</span>
            </div>
            <textarea id="sandboxCode" class="sandbox-textarea" placeholder="Digite seu código Python aqui..."></textarea>
          </div>
          <div class="sandbox-output-panel">
            <div class="panel-toolbar">
              <span><i class="fa-solid fa-terminal"></i> Console de Saída</span>
              <span id="execTimer" style="font-family: var(--font-code); font-size: 0.75rem; color: var(--accent-green);"></span>
            </div>
            <div id="sandboxTerminal" class="sandbox-terminal">
              <span class="term-system">Pyodide Python pronto para execução. Digite seu código e clique em Executar.</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- MODAL: Quizzes & Desafios -->
  <div class="modal-overlay" id="quizzesModal">
    <div class="modal-window" style="max-width: 850px;">
      <div class="modal-header">
        <div class="modal-title">
          <i class="fa-solid fa-brain" style="color: #fbbf24;"></i>
          <span>Quizzes & Testes de Conhecimento (+50 XP)</span>
        </div>
        <button class="modal-close-btn" onclick="closeModal('quizzesModal')"><i class="fa-solid fa-xmark"></i></button>
      </div>
      <div class="modal-body" id="quizzesModalBody">
        <!-- Injected dynamically -->
      </div>
    </div>
  </div>

  <!-- MODAL: Cheat Sheet -->
  <div class="modal-overlay" id="cheatSheetModal">
    <div class="modal-window" style="max-width: 950px;">
      <div class="modal-header">
        <div class="modal-title">
          <i class="fa-solid fa-bolt" style="color: #c084fc;"></i>
          <span>Guia Rápido de Referência (Cheat Sheet)</span>
        </div>
        <button class="modal-close-btn" onclick="closeModal('cheatSheetModal')"><i class="fa-solid fa-xmark"></i></button>
      </div>
      <div class="modal-body">
        <div class="tabs-nav" id="cheatTabsNav">
          <button class="tab-btn active" onclick="switchCheatTab('basics', this)">Sintaxe & Entrada/Saída</button>
          <button class="tab-btn" onclick="switchCheatTab('collections', this)">Listas, Dicionários & Tuplas</button>
          <button class="tab-btn" onclick="switchCheatTab('control_flow', this)">Condicionais, Loops & Erros</button>
          <button class="tab-btn" onclick="switchCheatTab('functions_oop', this)">Funções & Classes (POO)</button>
        </div>
        <div id="cheatSheetContent" class="cheatsheet-grid" style="margin-top: 1rem;">
          <!-- Injected dynamically -->
        </div>
      </div>
    </div>
  </div>

  <!-- MODAL: Anotações Rápidas -->
  <div class="modal-overlay" id="notesModal">
    <div class="modal-window" style="max-width: 800px;">
      <div class="modal-header">
        <div class="modal-title">
          <i class="fa-solid fa-pen-to-square" style="color: #34d399;"></i>
          <span>Bloco de Anotações de Estudo</span>
        </div>
        <div style="display: flex; gap: 0.6rem;">
          <button class="btn-action" onclick="downloadNotes()"><i class="fa-solid fa-download"></i> Exportar (.md)</button>
          <button class="modal-close-btn" onclick="closeModal('notesModal')"><i class="fa-solid fa-xmark"></i></button>
        </div>
      </div>
      <div class="modal-body">
        <p style="font-size: 0.85rem; color: var(--text-muted);">Suas anotações são salvas automaticamente no armazenamento local do navegador.</p>
        <textarea id="notesArea" class="notes-textarea" placeholder="Escreva aqui suas anotações, resumos, ideias ou dúvidas de estudo..."></textarea>
      </div>
    </div>
  </div>

  <script>
    // Embedded Data
    const FILE_TREE = ${treeJson};
    const ALL_FILES = ${filesJson};
    const QUIZZES = ${quizzesJson};
    const CHEATSHEET = ${cheatsheetJson};
    const SNIPPETS = ${snippetsJson};

    // State Management
    let currentCategory = 'all';
    let currentNavFilter = 'all'; // 'all', 'starred', 'completed'
    let currentTypeFilter = 'all';
    let currentSearchQuery = '';
    let currentViewMode = 'grid'; // 'grid' | 'list'
    let currentViewingFile = null;

    // User Progress in localStorage
    const STORAGE_KEY = 'meus_estudos_progress_v2';
    let userProgress = {
      starred: [],
      completed: [],
      xp: 0,
      level: 1,
      quizAnswers: {},
      notes: '',
      lastVisitDate: new Date().toDateString(),
      streak: 1
    };

    function loadUserProgress() {
      try {
        const saved = localStorage.getItem(STORAGE_KEY);
        if (saved) {
          userProgress = Object.assign(userProgress, JSON.parse(saved));
        }
      } catch (e) {
        console.warn('Erro ao carregar dados locais:', e);
      }
      checkStreak();
      updateUserStatsUI();
    }

    function saveUserProgress() {
      try {
        localStorage.setItem(STORAGE_KEY, JSON.stringify(userProgress));
      } catch (e) {}
      updateUserStatsUI();
    }

    function addXP(amount) {
      userProgress.xp += amount;
      userProgress.level = Math.floor(userProgress.xp / 200) + 1;
      saveUserProgress();
    }

    function checkStreak() {
      const today = new Date().toDateString();
      if (userProgress.lastVisitDate !== today) {
        const yesterday = new Date(Date.now() - 86400000).toDateString();
        if (userProgress.lastVisitDate === yesterday) {
          userProgress.streak += 1;
        } else {
          userProgress.streak = 1;
        }
        userProgress.lastVisitDate = today;
        saveUserProgress();
      }
    }

    function updateUserStatsUI() {
      const xpBadge = document.getElementById('userXpText');
      const levelBadge = document.getElementById('userLevelText');
      const countStarred = document.getElementById('countStarred');
      const countCompleted = document.getElementById('countCompleted');
      const countAll = document.getElementById('countAll');
      const progressPercent = document.getElementById('progressPercent');
      const progressBarFill = document.getElementById('progressBarFill');
      const progressCompletedText = document.getElementById('progressCompletedText');
      const streakText = document.getElementById('streakText');

      if (xpBadge) xpBadge.textContent = '(' + userProgress.xp + ' XP)';
      if (levelBadge) levelBadge.textContent = 'Nível ' + userProgress.level;
      if (countStarred) countStarred.textContent = userProgress.starred.length;
      if (countCompleted) countCompleted.textContent = userProgress.completed.length;
      if (countAll) countAll.textContent = ALL_FILES.length;
      if (streakText) streakText.textContent = '🔥 ' + userProgress.streak + ' ' + (userProgress.streak === 1 ? 'dia' : 'dias');

      const total = ALL_FILES.length;
      const completed = userProgress.completed.length;
      const pct = total > 0 ? Math.min(100, Math.round((completed / total) * 100)) : 0;
      if (progressPercent) progressPercent.textContent = pct + '%';
      if (progressBarFill) progressBarFill.style.width = pct + '%';
      if (progressCompletedText) progressCompletedText.textContent = completed + ' / ' + total + ' concluídos';
    }

    // Category Sidebar Render
    function renderCategoryNav() {
      const navList = document.getElementById('categoryNavList');
      if (!navList) return;

      const categories = [
        { name: 'Resumos Jupyter', icon: 'fa-book-open', color: '#fb923c' },
        { name: 'Jornada Python', icon: 'fa-route', color: '#c084fc' },
        { name: 'Curso em Vídeo', icon: 'fa-video', color: '#60a5fa' },
        { name: 'Cisco Python', icon: 'fa-network-wired', color: '#38bdf8' },
        { name: 'Mimo App', icon: 'fa-mobile-screen', color: '#34d399' },
        { name: 'Apostilas & PDFs', icon: 'fa-file-pdf', color: '#f472b6' },
        { name: 'JavaScript & Web', icon: 'fa-brands fa-js', color: '#facc15' }
      ];

      navList.innerHTML = '';
      categories.forEach(cat => {
        const count = ALL_FILES.filter(f => f.category === cat.name).length;
        const btn = document.createElement('button');
        btn.className = 'nav-btn' + (currentCategory === cat.name ? ' active' : '');
        btn.onclick = () => filterByCategory(cat.name);
        btn.innerHTML = \`
          <span class="nav-left"><i class="\${cat.icon}" style="color: \${cat.color};"></i> \${cat.name}</span>
          <span class="badge-count">\${count}</span>
        \`;
        navList.appendChild(btn);
      });
    }

    // Filter Logic
    function getFilteredFiles() {
      return ALL_FILES.filter(file => {
        // Nav filter
        if (currentNavFilter === 'starred' && !userProgress.starred.includes(file.path)) return false;
        if (currentNavFilter === 'completed' && !userProgress.completed.includes(file.path)) return false;

        // Category filter
        if (currentCategory !== 'all' && file.category !== currentCategory) return false;

        // Type filter
        if (currentTypeFilter !== 'all' && file.ext !== currentTypeFilter) return false;

        // Search Query
        if (currentSearchQuery) {
          const q = currentSearchQuery.toLowerCase();
          const matchName = file.name.toLowerCase().includes(q);
          const matchCat = file.category.toLowerCase().includes(q);
          const matchPath = file.path.toLowerCase().includes(q);
          if (!matchName && !matchCat && !matchPath) return false;
        }

        return true;
      });
    }

    function getFileBadgeClass(ext) {
      switch (ext) {
        case '.py': return { cls: 'badge-py', icon: 'fa-brands fa-python' };
        case '.ipynb': return { cls: 'badge-ipynb', icon: 'fa-solid fa-book-open' };
        case '.md': return { cls: 'badge-md', icon: 'fa-brands fa-markdown' };
        case '.pdf': return { cls: 'badge-pdf', icon: 'fa-solid fa-file-pdf' };
        case '.html': return { cls: 'badge-html', icon: 'fa-brands fa-html5' };
        default: return { cls: 'badge-generic', icon: 'fa-solid fa-file' };
      }
    }

    // Render Explorer View
    function renderView() {
      const container = document.getElementById('contentContainer');
      const breadcrumbCurrent = document.getElementById('currentBreadcrumb');
      const files = getFilteredFiles();

      // Update breadcrumb
      if (breadcrumbCurrent) {
        if (currentSearchQuery) {
          breadcrumbCurrent.textContent = 'Busca: "' + currentSearchQuery + '" (' + files.length + ')';
        } else if (currentNavFilter === 'starred') {
          breadcrumbCurrent.textContent = 'Meus Favoritos (' + files.length + ')';
        } else if (currentNavFilter === 'completed') {
          breadcrumbCurrent.textContent = 'Aulas Concluídas (' + files.length + ')';
        } else if (currentCategory !== 'all') {
          breadcrumbCurrent.textContent = currentCategory + ' (' + files.length + ')';
        } else {
          breadcrumbCurrent.textContent = 'Todos os Conteúdos (' + files.length + ')';
        }
      }

      if (!files || files.length === 0) {
        container.innerHTML = \`
          <div class="empty-state">
            <i class="fa-solid fa-folder-open"></i>
            <h3>Nenhum conteúdo encontrado</h3>
            <p>Tente ajustar os filtros, categoria ou termo de busca.</p>
            <button class="btn-action active" onclick="navigateToRoot()">Ver Todos os Arquivos</button>
          </div>
        \`;
        return;
      }

      if (currentViewMode === 'grid') {
        let gridHtml = '<div class="study-grid">';
        files.forEach(file => {
          const badge = getFileBadgeClass(file.ext);
          const isStarred = userProgress.starred.includes(file.path);
          const isCompleted = userProgress.completed.includes(file.path);

          gridHtml += \`
            <div class="study-card" onclick="openFileInReader('\${file.path.replace(/'/g, "\\\\'")}')">
              <div class="card-top">
                <div class="card-icon-badge \${badge.cls}">
                  <i class="\${badge.icon}"></i>
                </div>
                <div class="card-quick-actions" onclick="event.stopPropagation()">
                  <button class="card-action-btn \${isStarred ? 'starred' : ''}" title="Favoritar" onclick="toggleStar('\${file.path.replace(/'/g, "\\\\'")}')">
                    <i class="\${isStarred ? 'fa-solid' : 'fa-regular'} fa-star"></i>
                  </button>
                  <button class="card-action-btn \${isCompleted ? 'completed' : ''}" title="Concluído" onclick="toggleComplete('\${file.path.replace(/'/g, "\\\\'")}')">
                    <i class="\${isCompleted ? 'fa-solid' : 'fa-regular'} fa-circle-check"></i>
                  </button>
                </div>
              </div>
              <div class="card-body">
                <div class="card-title" title="\${escapeHtml(file.name)}">\${escapeHtml(file.name)}</div>
                <div class="card-category">\${file.category}</div>
              </div>
              <div class="card-footer">
                <span class="card-tag">\${file.ext.replace('.', '').toUpperCase() || 'ARQUIVO'}</span>
                <span>\${file.sizeFormatted}</span>
              </div>
            </div>
          \`;
        });
        gridHtml += '</div>';
        container.innerHTML = gridHtml;
      } else {
        let tableHtml = \`
          <div class="study-table-container">
            <table class="study-table">
              <thead>
                <tr>
                  <th style="width: 40px;"></th>
                  <th>Nome do Arquivo</th>
                  <th>Trilha / Categoria</th>
                  <th>Formato</th>
                  <th>Tamanho</th>
                  <th style="text-align: right;">Ações</th>
                </tr>
              </thead>
              <tbody>
        \`;
        files.forEach(file => {
          const badge = getFileBadgeClass(file.ext);
          const isStarred = userProgress.starred.includes(file.path);
          const isCompleted = userProgress.completed.includes(file.path);

          tableHtml += \`
            <tr onclick="openFileInReader('\${file.path.replace(/'/g, "\\\\'")}')">
              <td>
                <i class="\${badge.icon}" style="font-size: 1.1rem;"></i>
              </td>
              <td style="font-weight: 500;">
                \${escapeHtml(file.name)}
                \${isCompleted ? ' <i class="fa-solid fa-circle-check" style="color:#34d399; font-size:0.8rem;"></i>' : ''}
              </td>
              <td style="color: var(--text-muted);">\${file.category}</td>
              <td><span class="card-tag">\${file.ext.replace('.', '').toUpperCase()}</span></td>
              <td style="color: var(--text-dim); font-family: var(--font-code); font-size: 0.8rem;">\${file.sizeFormatted}</td>
              <td style="text-align: right;" onclick="event.stopPropagation()">
                <button class="card-action-btn \${isStarred ? 'starred' : ''}" style="display:inline-flex;" onclick="toggleStar('\${file.path.replace(/'/g, "\\\\'")}')">
                  <i class="\${isStarred ? 'fa-solid' : 'fa-regular'} fa-star"></i>
                </button>
              </td>
            </tr>
          \`;
        });
        tableHtml += '</tbody></table></div>';
        container.innerHTML = tableHtml;
      }
    }

    // Navigation & Filtering Handlers
    function navigateToRoot() {
      currentCategory = 'all';
      currentNavFilter = 'all';
      currentTypeFilter = 'all';
      currentSearchQuery = '';
      const sInput = document.getElementById('globalSearch');
      if (sInput) sInput.value = '';
      
      document.querySelectorAll('.filter-pill').forEach((p, idx) => {
        p.classList.toggle('active', idx === 0);
      });
      document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
      const navAll = document.getElementById('navAll');
      if (navAll) navAll.classList.add('active');

      renderCategoryNav();
      renderView();
    }

    function filterByNav(filter) {
      currentNavFilter = filter;
      currentCategory = 'all';
      document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
      if (filter === 'all') document.getElementById('navAll')?.classList.add('active');
      if (filter === 'starred') document.getElementById('navStarred')?.classList.add('active');
      if (filter === 'completed') document.getElementById('navCompleted')?.classList.add('active');
      renderCategoryNav();
      renderView();
    }

    function filterByCategory(catName) {
      currentCategory = catName;
      currentNavFilter = 'all';
      document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
      renderCategoryNav();
      renderView();
    }

    function setTypeFilter(ext, btn) {
      currentTypeFilter = ext;
      document.querySelectorAll('.filter-pill').forEach(p => p.classList.remove('active'));
      if (btn) btn.classList.add('active');
      renderView();
    }

    function setViewMode(mode) {
      currentViewMode = mode;
      document.getElementById('btnViewGrid')?.classList.toggle('active', mode === 'grid');
      document.getElementById('btnViewList')?.classList.toggle('active', mode === 'list');
      renderView();
    }

    // Star & Complete Actions
    function toggleStar(filePath) {
      const idx = userProgress.starred.indexOf(filePath);
      if (idx >= 0) {
        userProgress.starred.splice(idx, 1);
      } else {
        userProgress.starred.push(filePath);
      }
      saveUserProgress();
      renderView();
    }

    function toggleComplete(filePath) {
      const idx = userProgress.completed.indexOf(filePath);
      if (idx >= 0) {
        userProgress.completed.splice(idx, 1);
      } else {
        userProgress.completed.push(filePath);
        addXP(100);
      }
      saveUserProgress();
      renderView();
      if (currentViewingFile && currentViewingFile.path === filePath) {
        updateReaderCompleteBtn();
      }
    }

    function toggleCurrentFileComplete() {
      if (currentViewingFile) {
        toggleComplete(currentViewingFile.path);
      }
    }

    function updateReaderCompleteBtn() {
      const btn = document.getElementById('readerToggleCompleteBtn');
      if (!btn || !currentViewingFile) return;
      const isCompleted = userProgress.completed.includes(currentViewingFile.path);
      btn.className = 'btn-action' + (isCompleted ? ' active' : '');
      btn.innerHTML = isCompleted ? '<i class="fa-solid fa-circle-check"></i> Concluído' : '<i class="fa-regular fa-circle-check"></i> Marcar Concluído';
    }

    // Reader Implementation
    async function openFileInReader(filePath) {
      const file = ALL_FILES.find(f => f.path === filePath);
      if (!file) return;

      currentViewingFile = file;
      const modal = document.getElementById('readerModal');
      const body = document.getElementById('readerModalBody');
      const titleEl = document.getElementById('readerFileName');
      const iconEl = document.getElementById('readerFileIcon');
      const extLink = document.getElementById('readerExternalLink');
      const sandboxBtn = document.getElementById('readerOpenSandboxBtn');

      if (titleEl) titleEl.textContent = file.name;
      if (extLink) extLink.href = file.viewerUrl || file.path;
      if (iconEl) {
        const badge = getFileBadgeClass(file.ext);
        iconEl.className = badge.icon;
      }
      updateReaderCompleteBtn();

      // Show sandbox button for python code
      if (sandboxBtn) {
        sandboxBtn.style.display = (file.ext === '.py') ? 'flex' : 'none';
      }

      body.innerHTML = '<div style="display:flex; justify-content:center; align-items:center; height:300px; color:var(--primary); font-size:1.5rem;"><i class="fa-solid fa-spinner fa-spin"></i> &nbsp; Carregando aula...</div>';
      openModal('readerModal');

      try {
        const response = await fetch(file.path);
        if (!response.ok) {
          body.innerHTML = \`<div class="reader-container"><p>Não foi possível carregar o arquivo diretamente. <a href="\${file.path}" target="_blank" style="color:var(--primary)">Clique aqui para abrir externamente</a>.</p></div>\`;
          return;
        }

        if (file.ext === '.ipynb') {
          const nb = await response.json();
          renderNotebookInModal(nb, body);
        } else if (file.ext === '.md') {
          const mdText = await response.text();
          body.innerHTML = \`<div class="reader-container">\${marked.parse(mdText)}</div>\`;
          hljs.highlightAll();
        } else if (file.ext === '.py') {
          const pyCode = await response.text();
          body.innerHTML = \`
            <div class="reader-container">
              <pre><code class="language-python" id="modalPyCode">\${escapeHtml(pyCode)}</code></pre>
            </div>
          \`;
          hljs.highlightAll();
        } else if (file.ext === '.pdf') {
          body.innerHTML = \`<iframe src="\${file.path}" style="width:100%; height:100%; border:none; border-radius:8px;"></iframe>\`;
        } else if (file.ext === '.html') {
          body.innerHTML = \`<iframe src="\${file.path}" style="width:100%; height:100%; border:none; border-radius:8px;"></iframe>\`;
        } else {
          const txt = await response.text();
          body.innerHTML = \`<pre style="padding:1rem; font-family:var(--font-code); color:#cbd5e1;">\${escapeHtml(txt)}</pre>\`;
        }
      } catch (err) {
        body.innerHTML = \`
          <div class="reader-container">
            <p>Visualização nativa carregada via fallback. <a href="\${file.viewerUrl}" target="_blank" style="color:var(--primary)">Abrir no visualizador dedicado</a>.</p>
            <iframe src="\${file.viewerUrl}" style="width:100%; height:600px; border:none; border-radius:8px;"></iframe>
          </div>
        \`;
      }
    }

    function renderNotebookInModal(nb, container) {
      let html = '<div class="reader-container">';
      (nb.cells || []).forEach((cell, idx) => {
        const source = Array.isArray(cell.source) ? cell.source.join('') : (cell.source || '');
        if (cell.cell_type === 'markdown') {
          html += \`<div class="nb-cell">\${marked.parse(source)}</div>\`;
        } else if (cell.cell_type === 'code') {
          const escaped = escapeHtml(source);
          html += \`
            <div class="nb-cell nb-cell-code">
              <button class="btn-run-cell" onclick="runCellCode(this)">
                <i class="fa-solid fa-play"></i> Executar
              </button>
              <pre><code class="language-python">\${escaped}</code></pre>
          \`;
          const outputs = cell.outputs || [];
          if (outputs.length > 0) {
            let outText = '';
            outputs.forEach(out => {
              if (out.output_type === 'stream') {
                outText += Array.isArray(out.text) ? out.text.join('') : (out.text || '');
              } else if (out.data && out.data['text/plain']) {
                const plain = out.data['text/plain'];
                outText += Array.isArray(plain) ? plain.join('') : plain;
              }
            });
            if (outText.trim()) {
              html += \`<div class="nb-cell-output">\${escapeHtml(outText)}</div>\`;
            }
          }
          html += '</div>';
        }
      });
      html += '</div>';
      container.innerHTML = html;
      hljs.highlightAll();
    }

    function runCellCode(btn) {
      const pre = btn.closest('.nb-cell-code').querySelector('pre code');
      if (!pre) return;
      const code = pre.innerText;
      openSandboxModal();
      document.getElementById('sandboxCode').value = code;
      runSandboxCode();
    }

    function openCurrentInSandbox() {
      const codeEl = document.getElementById('modalPyCode');
      if (codeEl) {
        const code = codeEl.innerText;
        closeModal('readerModal');
        openSandboxModal();
        document.getElementById('sandboxCode').value = code;
        runSandboxCode();
      }
    }

    // Modal Control
    function openModal(id) {
      const el = document.getElementById(id);
      if (el) el.classList.add('active');
    }

    function closeModal(id) {
      const el = document.getElementById(id);
      if (el) el.classList.remove('active');
    }

    // Pyodide Python 3 Sandbox
    let pyodideInstance = null;
    let isPyodideLoading = false;

    async function getPyodide() {
      if (pyodideInstance) return pyodideInstance;
      if (isPyodideLoading) {
        while (isPyodideLoading) {
          await new Promise(r => setTimeout(r, 200));
        }
        return pyodideInstance;
      }
      isPyodideLoading = true;
      const term = document.getElementById('sandboxTerminal');
      if (term) term.innerHTML = '<span class="term-system">⏳ Inicializando interpretador WebAssembly Python 3...</span>';
      try {
        pyodideInstance = await loadPyodide({
          stdout: (text) => appendTerminal(text),
          stderr: (text) => appendTerminal(text, 'term-error')
        });
        if (term) term.innerHTML += '<br><span class="term-success">✅ Interpretador Python 3.12 carregado com sucesso!</span><br>';
      } catch (e) {
        if (term) term.innerHTML = '<span class="term-error">Erro ao carregar Pyodide: ' + escapeHtml(e.message) + '</span>';
      } finally {
        isPyodideLoading = false;
      }
      return pyodideInstance;
    }

    function appendTerminal(text, cls = '') {
      const term = document.getElementById('sandboxTerminal');
      if (!term) return;
      const span = document.createElement('span');
      if (cls) span.className = cls;
      span.textContent = text + '\\n';
      term.appendChild(span);
      term.scrollTop = term.scrollHeight;
    }

    function clearTerminal() {
      const term = document.getElementById('sandboxTerminal');
      if (term) term.innerHTML = '<span class="term-system">Terminal limpo.</span><br>';
    }

    async function runSandboxCode() {
      const code = document.getElementById('sandboxCode')?.value || '';
      const timerEl = document.getElementById('execTimer');
      const term = document.getElementById('sandboxTerminal');

      if (!code.trim()) return;

      term.innerHTML = '<span class="term-system">▶ Executando script...</span><br>';
      const startTime = performance.now();

      try {
        const py = await getPyodide();
        if (!py) return;
        const result = await py.runPythonAsync(code);
        const elapsed = (performance.now() - startTime).toFixed(0);
        if (timerEl) timerEl.textContent = elapsed + 'ms';
        if (result !== undefined) {
          appendTerminal('=> ' + String(result), 'term-success');
        }
        addXP(20);
      } catch (err) {
        appendTerminal(err.message, 'term-error');
      }
    }

    function openSandboxModal() {
      openModal('sandboxModal');
      getPyodide(); // warm up
      const sel = document.getElementById('snippetSelect');
      if (sel && sel.options.length <= 1) {
        SNIPPETS.forEach((s, idx) => {
          const opt = document.createElement('option');
          opt.value = idx;
          opt.textContent = s.name;
          sel.appendChild(opt);
        });
      }
    }

    function loadSnippet(idx) {
      if (idx === '') return;
      const snip = SNIPPETS[idx];
      if (snip) {
        document.getElementById('sandboxCode').value = snip.code;
      }
    }

    // Quizzes Implementation
    function openQuizzesModal() {
      renderQuizzes();
      openModal('quizzesModal');
    }

    function renderQuizzes() {
      const container = document.getElementById('quizzesModalBody');
      if (!container) return;

      let html = '';
      QUIZZES.forEach(qGroup => {
        html += \`
          <div style="margin-bottom: 2rem;">
            <h3 style="color: var(--primary); margin-bottom: 1rem;"><i class="fa-solid fa-list-check"></i> \${qGroup.title}</h3>
        \`;
        qGroup.questions.forEach((q, qIdx) => {
          const qId = qGroup.id + '-' + qIdx;
          const userAns = userProgress.quizAnswers[qId];

          html += \`
            <div class="quiz-card" style="margin-bottom: 1rem;">
              <div class="quiz-question-text">\${qIdx + 1}. \${q.question}</div>
              <div class="quiz-options">
          \`;

          q.options.forEach((opt, optIdx) => {
            let btnClass = 'quiz-option-btn';
            if (userAns !== undefined) {
              if (optIdx === q.answer) btnClass += ' correct';
              else if (userAns === optIdx) btnClass += ' incorrect';
            }

            html += \`
              <button class="\${btnClass}" \${userAns !== undefined ? 'disabled' : ''} onclick="answerQuiz('\${qId}', \${optIdx}, \${q.answer})">
                <i class="fa-regular fa-circle"></i> \${escapeHtml(opt)}
              </button>
            \`;
          });

          html += '</div>';

          if (userAns !== undefined) {
            html += \`
              <div class="quiz-explanation">
                <strong>\${userAns === q.answer ? '🎉 Correto!' : '❌ Incorreto.'}</strong> \${q.explanation}
              </div>
            \`;
          }

          html += '</div>';
        });
        html += '</div>';
      });

      container.innerHTML = html;
    }

    function answerQuiz(qId, selectedIdx, correctIdx) {
      userProgress.quizAnswers[qId] = selectedIdx;
      if (selectedIdx === correctIdx) {
        addXP(50);
      }
      saveUserProgress();
      renderQuizzes();
    }

    // Cheat Sheet Implementation
    function openCheatSheetModal() {
      switchCheatTab('basics', document.querySelector('.tab-btn'));
      openModal('cheatSheetModal');
    }

    function switchCheatTab(tabKey, btn) {
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      if (btn) btn.classList.add('active');

      const container = document.getElementById('cheatSheetContent');
      if (!container) return;

      const items = CHEATSHEET[tabKey] || [];
      let html = '';
      items.forEach(item => {
        html += \`
          <div class="cheatsheet-card">
            <h4>\${escapeHtml(item.title)}</h4>
            <pre style="background:#090d16; padding:0.85rem; border-radius:6px; font-family:var(--font-code); font-size:0.85rem; color:#f8fafc; overflow-x:auto;"><code>\${escapeHtml(item.code)}</code></pre>
          </div>
        \`;
      });
      container.innerHTML = html;
    }

    // Notes Modal
    function openNotesModal() {
      const area = document.getElementById('notesArea');
      if (area) {
        area.value = userProgress.notes || '';
        area.oninput = (e) => {
          userProgress.notes = e.target.value;
          saveUserProgress();
        };
      }
      openModal('notesModal');
    }

    function downloadNotes() {
      const content = userProgress.notes || '# Minhas Anotações de Estudo\\n';
      const blob = new Blob([content], { type: 'text/markdown;charset=utf-8;' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'meus-estudos-anotacoes.md';
      a.click();
      URL.revokeObjectURL(url);
    }

    // Pomodoro Timer
    let pomoSeconds = 25 * 60;
    let pomoTimerId = null;
    let isPomoRunning = false;

    function formatPomoTime(sec) {
      const m = Math.floor(sec / 60).toString().padStart(2, '0');
      const s = (sec % 60).toString().padStart(2, '0');
      return m + ':' + s;
    }

    function togglePomodoro() {
      const btn = document.getElementById('pomoToggleBtn');
      if (isPomoRunning) {
        clearInterval(pomoTimerId);
        isPomoRunning = false;
        if (btn) btn.innerHTML = '<i class="fa-solid fa-play"></i>';
      } else {
        isPomoRunning = true;
        if (btn) btn.innerHTML = '<i class="fa-solid fa-pause"></i>';
        pomoTimerId = setInterval(() => {
          pomoSeconds--;
          document.getElementById('pomoTime').textContent = formatPomoTime(pomoSeconds);
          if (pomoSeconds <= 0) {
            clearInterval(pomoTimerId);
            isPomoRunning = false;
            if (btn) btn.innerHTML = '<i class="fa-solid fa-play"></i>';
            alert('🍅 Ciclo Pomodoro concluído! Hora de uma pausa de 5 minutos. (+150 XP)');
            addXP(150);
            pomoSeconds = 25 * 60;
            document.getElementById('pomoTime').textContent = '25:00';
          }
        }, 1000);
      }
    }

    function resetPomodoro() {
      clearInterval(pomoTimerId);
      isPomoRunning = false;
      pomoSeconds = 25 * 60;
      document.getElementById('pomoTime').textContent = '25:00';
      const btn = document.getElementById('pomoToggleBtn');
      if (btn) btn.innerHTML = '<i class="fa-solid fa-play"></i>';
    }

    // Global Search & Keyboard Shortcuts
    document.addEventListener('DOMContentLoaded', () => {
      loadUserProgress();
      renderCategoryNav();
      renderView();

      const searchInput = document.getElementById('globalSearch');
      if (searchInput) {
        searchInput.addEventListener('input', (e) => {
          currentSearchQuery = e.target.value;
          renderView();
        });
      }

      // Keyboard Shortcuts
      window.addEventListener('keydown', (e) => {
        if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
          e.preventDefault();
          document.getElementById('globalSearch')?.focus();
        } else if (e.altKey && e.key.toLowerCase() === 's') {
          e.preventDefault();
          openSandboxModal();
        } else if (e.key === 'Escape') {
          document.querySelectorAll('.modal-overlay.active').forEach(m => m.classList.remove('active'));
        }
      });
    });

    function escapeHtml(str) {
      if (!str) return '';
      return String(str)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#039;');
    }
  </script>
</body>
</html>`;
}

// Build execution
console.log('🚀 Iniciando geração do Dashboard Meus Estudos...');
const { tree, allFilesList } = buildFileTree(ROOT_DIR);
console.log(`📁 Indexados ${allFilesList.length} arquivos de estudo.`);

const html = generateAppHtml(tree, allFilesList);
const outputPath = path.join(ROOT_DIR, 'index.html');
fs.writeFileSync(outputPath, html, 'utf-8');

console.log(`✅ Dashboard gerado com sucesso em: ${outputPath}`);
