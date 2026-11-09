# 🐍 Meus Estudos (`meus-estudos`) — Hub Interativo de Programação (Python, JavaScript & HTML)

Repositório central de estudos, exercícios práticos, notebooks interativos e dashboard web de acompanhamento da evolução em **Python**, **JavaScript** e **Desenvolvimento Web**.

---

## 🚀 Principais Módulos do Repositório

### 1. 🌐 Plataforma Web Interativa (`py-estudos/` & `index.html`)
- **Dashboard Geral (`index.html` gerado por `build_dashboard.js` / `build_dashboard.py`)**:
  - Visualizador unificado de todas as aulas, desafios e laboratórios com páginas estáticas em `.viewers/`.
- **App React de Estudos (`py-estudos/`)**:
  - Construído com **React + TypeScript + Vite**.
  - Inclui **Leitor de Jupyter Notebooks (`NotebookReader.tsx`)**, **Sandbox Python Interativo (`PythonSandbox.tsx`)**, **Quizzes de Fixação (`QuizPanel.tsx`)** e **Painel de Progresso (`StatsPanel.tsx`)**.

### 2. 📚 Trilhas de Conhecimento
- **`cisco_fundamentos_python/`**: Laboratórios e módulos completos do curso *Python Essentials 1 & 2* (Cisco Networking Academy).
- **`cursoemvideo_python/`**: Mais de 115 desafios resolvidos e aulas práticas dos Mundos 1, 2 e 3 de Python 3 (Curso em Vídeo - Gustavo Guanabara).
- **`Jornada Python/` & `Resumos/`**: 23 guias em Markdown e Jupyter Notebooks (`.ipynb`) cobrindo desde variáveis e estruturas de dados até POO, tratamento de erros, manipulação de arquivos e consumo de APIs com `requests`.
- **`mimo_app/`**: Trilhas práticas de **Python** e **HTML5** (aulas, desafios e projetos).

---

## 📂 Estrutura do Repositório

```text
meus-estudos/
├── cisco_fundamentos_python/   # Python Essentials 1 e 2 (Cisco)
├── cursoemvideo_python/        # Aulas e 115 exercícios resolvidos (Mundos 1, 2 e 3)
├── Jornada Python/             # 23 apostilas em Markdown
├── mimo_app/                   # Trilhas de HTML e Python (Aulas, Desafios e Projetos)
├── py-estudos/                 # Aplicação React + TypeScript + Vite com Sandbox e Quizzes
├── Python/                     # Materiais visuais e resumos em HTML/PDF
├── Resumos/                    # 21 Jupyter Notebooks (.ipynb) detalhados
├── .viewers/                   # Páginas HTML geradas para leitura rápida dos códigos
├── build_dashboard.js          # Gerador do painel unificado
├── index.html                  # Dashboard principal navegável
└── README.md
```

---

## 💻 Como Executar o App Interativo (`py-estudos`)

```bash
cd py-estudos
npm install
npm run dev
```

Ou abra diretamente o arquivo `index.html` na raiz do repositório para navegar pelo Dashboard de Estudos.
