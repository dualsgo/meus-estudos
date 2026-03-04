import type { Module, Progress, Quiz } from './types';

export const MODULES: Module[] = [
    { id: '01', number: 1, title: 'Introdução ao Python', filename: '01_introducao.ipynb', status: 'completed' },
    { id: '02', number: 2, title: 'Variáveis', filename: '02_variaveis.ipynb', status: 'completed' },
    { id: '03', number: 3, title: 'Tipos de Dados', filename: '03_tipos_de_dados.ipynb', status: 'completed' },
    { id: '04', number: 4, title: 'Operadores', filename: '04_operadores.ipynb', status: 'current' },
    { id: '05', number: 5, title: 'Funções Básicas', filename: '05_funcoes_basicas.ipynb', status: 'locked' },
    { id: '06', number: 6, title: 'Manipulando Texto', filename: '06_manipulando_texto.ipynb', status: 'locked' },
    { id: '07', number: 7, title: 'Estruturas de Controle', filename: '07_estruturas_de_controle.ipynb', status: 'locked' },
    { id: '08', number: 8, title: 'Estruturas de Repetição', filename: '08_estruturas_de_repeticao.ipynb', status: 'locked' },
    { id: '09', number: 9, title: 'Funções', filename: '09_funcoes.ipynb', status: 'locked' },
    { id: '10', number: 10, title: 'Mais Funções', filename: '10_mais_funcoes.ipynb', status: 'locked' },
    { id: '11', number: 11, title: 'Listas', filename: '11_listas.ipynb', status: 'locked' },
    { id: '12', number: 12, title: 'Mais Listas', filename: '12_mais_listas.ipynb', status: 'locked' },
    { id: '13', number: 13, title: 'Bubble Sort', filename: '13_bubblesort.ipynb', status: 'locked' },
    { id: '14', number: 14, title: 'Funções, Loops e Listas', filename: '14_funcoes_loops_listas.ipynb', status: 'locked' },
    { id: '15', number: 15, title: 'Tuplas', filename: '15_tuplas.ipynb', status: 'locked' },
    { id: '16', number: 16, title: 'Dicionários', filename: '16_dicionarios.ipynb', status: 'locked' },
    { id: '17', number: 17, title: 'Conjuntos', filename: '17_conjuntos.ipynb', status: 'locked' },
    { id: '18', number: 18, title: 'Classes e OOP', filename: '18_classes.ipynb', status: 'locked' },
    { id: '19', number: 19, title: 'Tratamento de Erros', filename: '19_erros.ipynb', status: 'locked' },
    { id: '20', number: 20, title: 'APIs', filename: '20_API.ipynb', status: 'locked' },
];

export const QUIZZES: Record<string, Quiz[]> = {
    '01': [
        {
            question: 'O que é Python?',
            options: ['Uma linguagem compilada de baixo nível', 'Uma linguagem interpretada e de alto nível', 'Um banco de dados relacional', 'Um sistema operacional'],
            correctIndex: 1,
            explanation: 'Python é uma linguagem de alto nível e interpretada, projetada para ser legível e de propósito geral.',
        },
        {
            question: 'Quem criou o Python?',
            options: ['Linus Torvalds', 'Dennis Ritchie', 'Guido van Rossum', 'James Gosling'],
            correctIndex: 2,
            explanation: 'Python foi criado pelo matemático holandês Guido van Rossum em 1991.',
        },
        {
            question: 'O que torna a indentação especial em Python?',
            options: ['É apenas estética', 'Define blocos de código (sintaxe obrigatória)', 'É ignorada pelo interpretador', 'Serve apenas para comentários'],
            correctIndex: 1,
            explanation: 'Em Python, a indentação é sintaxe obrigatória. Ela define onde começa e termina um bloco de código.',
        },
        {
            question: 'Qual versão do Python deve ser usada por iniciantes?',
            options: ['Python 1', 'Python 2', 'Python 3', 'Qualquer versão'],
            correctIndex: 2,
            explanation: 'Python 2 foi descontinuado em 2020. Iniciantes devem focar exclusivamente no Python 3.',
        },
        {
            question: 'O que significa "Batteries Included" no contexto do Python?',
            options: ['O Python gasta muita energia', 'Vem com uma grande biblioteca padrão', 'Requer uma fonte de energia especial', 'É uma linguagem lenta'],
            correctIndex: 1,
            explanation: 'O Python vem com uma gigantesca biblioteca padrão embutida, dispensando código do zero para tarefas comuns.',
        },
    ],
    '02': [
        {
            question: 'Como você cria uma variável em Python?',
            options: ['var x = 10', 'int x = 10', 'x = 10', 'declare x = 10'],
            correctIndex: 2,
            explanation: 'Em Python não há palavra reservada para declarar variáveis, basta usar o operador de atribuição: x = 10',
        },
        {
            question: 'Qual das opções é um nome de variável INVÁLIDO em Python?',
            options: ['minha_variavel', '_privada', '2contador', 'camelCase'],
            correctIndex: 2,
            explanation: 'Nomes de variáveis não podem começar com números. "2contador" é inválido.',
        },
        {
            question: 'O que acontece se você usar o mesmo nome de variável duas vezes?',
            options: ['Gera um erro', 'Cria uma nova variável separada', 'O valor antigo é sobrescrito', 'O Python pergunta o que fazer'],
            correctIndex: 2,
            explanation: 'Em Python, reatribuir um nome de variável substitui (sobrescreve) o valor anterior.',
        },
    ],
    '03': [
        {
            question: 'Qual é o tipo de dado de `3.14` em Python?',
            options: ['int', 'float', 'str', 'bool'],
            correctIndex: 1,
            explanation: 'Números com casas decimais são do tipo `float` em Python.',
        },
        {
            question: 'Como você verifica o tipo de uma variável em Python?',
            options: ['typeOf(x)', 'x.type()', 'type(x)', 'typeof x'],
            correctIndex: 2,
            explanation: 'A função built-in `type()` retorna o tipo de um objeto: `type(x)`.',
        },
        {
            question: 'Qual é o resultado de `type(True)` em Python?',
            options: ['<class \'int\'>', '<class \'bool\'>', '<class \'str\'>', '<class \'NoneType\'>'],
            correctIndex: 1,
            explanation: '`True` e `False` são do tipo `bool` (booleano) em Python.',
        },
    ],
    '04': [
        {
            question: 'Qual operador verifica se dois valores são IGUAIS em Python?',
            options: ['=', '==', '!=', '==='],
            correctIndex: 1,
            explanation: '`=` é atribuição. Para comparar igualdade usamos `==` (dois sinais de igual).',
        },
        {
            question: 'Qual é o resultado de `10 // 3` em Python?',
            options: ['3.33', '3', '1', '0'],
            correctIndex: 1,
            explanation: '`//` é divisão inteira. 10 dividido por 3 é 3 com resto 1. O resultado é 3 (sem casas decimais).',
        },
        {
            question: 'O que o operador `%` retorna?',
            options: ['A porcentagem', 'O quociente', 'O resto da divisão', 'O resultado decimal'],
            correctIndex: 2,
            explanation: '`%` é o operador módulo. Ele retorna o RESTO da divisão inteira. Ex: `14 % 4 = 2`.',
        },
        {
            question: 'Qual é o resultado de `2 ** 8`?',
            options: ['16', '256', '64', '128'],
            correctIndex: 1,
            explanation: '`**` é exponenciação. 2 elevado a 8 = 256 (2^8).',
        },
        {
            question: 'O que `+=` faz em Python?',
            options: ['Testa se dois valores são iguais', 'Adiciona e atribui: x += 1 equivale a x = x + 1', 'Concatena strings permanentemente', 'Incrementa apenas strings'],
            correctIndex: 1,
            explanation: '`+=` é um operador de atribuição combinado. `x += 1` é a forma abreviada de `x = x + 1`.',
        },
    ],
    '05': [
        {
            question: 'Qual função exibe texto na tela em Python?',
            options: ['display()', 'console.log()', 'print()', 'echo()'],
            correctIndex: 2,
            explanation: '`print()` é a função built-in do Python para exibir informações na saída padrão (tela).',
        },
        {
            question: 'Qual função lê dados digitados pelo usuário?',
            options: ['read()', 'input()', 'scan()', 'get()'],
            correctIndex: 1,
            explanation: '`input()` pausa a execução, espera o usuário digitar algo e pressionar Enter, retornando uma string.',
        },
        {
            question: 'O que `len("Python")` retorna?',
            options: ['Python', '5', '6', 'True'],
            correctIndex: 2,
            explanation: '`len()` retorna o número de caracteres de uma string. "Python" tem 6 letras → retorna 6.',
        },
    ],
    '07': [
        {
            question: 'Qual é a sintaxe correta de um `if` em Python?',
            options: ['if (x > 5) { }', 'if x > 5 then', 'if x > 5:', 'IF x > 5 THEN'],
            correctIndex: 2,
            explanation: 'Em Python, o `if` não usa parênteses obrigatórios nem chaves. A sintaxe é `if condição:` seguida de bloco indentado.',
        },
        {
            question: 'Qual palavra é usada para "caso contrário" em Python?',
            options: ['otherwise', 'default', 'except', 'else'],
            correctIndex: 3,
            explanation: '`else` é usado para o bloco que executa quando a condição do `if` é falsa.',
        },
        {
            question: 'O que significa `elif` em Python?',
            options: ['Else if — outra condição a verificar', 'Execute later if — execução atrasada', 'Elseif — apenas um atalho visual', 'Evaluate if — garante avaliação'],
            correctIndex: 0,
            explanation: '`elif` é a abreviação de "else if". Permite verificar múltiplas condições em sequência.',
        },
    ],
    '08': [
        {
            question: 'Qual loop itera sobre itens de uma lista diretamente?',
            options: ['while', 'for', 'do-while', 'repeat'],
            correctIndex: 1,
            explanation: 'O loop `for` do Python é projetado para percorrer coleções: `for item in lista:`',
        },
        {
            question: 'O que `break` faz dentro de um loop?',
            options: ['Pausa o loop por 1 segundo', 'Pula para a próxima iteração', 'Encerra o loop imediatamente', 'Reinicia o loop do zero'],
            correctIndex: 2,
            explanation: '`break` encerra o loop completamente, saindo imediatamente da estrutura de repetição.',
        },
        {
            question: 'O que `range(5)` gera?',
            options: ['[1, 2, 3, 4, 5]', '[0, 1, 2, 3, 4]', '[0, 1, 2, 3, 4, 5]', '[5]'],
            correctIndex: 1,
            explanation: '`range(5)` gera números de 0 a 4 (começa em 0, termina antes de 5): 0, 1, 2, 3, 4.',
        },
    ],
    '09': [
        {
            question: 'Como você define uma função em Python?',
            options: ['function nome():', 'def nome():', 'func nome():', 'define nome():'],
            correctIndex: 1,
            explanation: 'Funções em Python são definidas com a palavra reservada `def` seguida do nome e parênteses.',
        },
        {
            question: 'O que é um parâmetro de função?',
            options: ['O valor retornado pela função', 'Uma variável recebida pela função na definição', 'O nome da função', 'Um tipo especial de loop'],
            correctIndex: 1,
            explanation: 'Parâmetros são variáveis declaradas na definição da função. Argumentos são os valores passados na chamada.',
        },
        {
            question: 'O que `return` faz em uma função?',
            options: ['Imprime o valor na tela', 'Para a função e devolve um valor', 'Reinicia a função', 'Cria uma nova variável global'],
            correctIndex: 1,
            explanation: '`return` encerra a execução da função e devolve um valor para quem a chamou.',
        },
    ],
    '11': [
        {
            question: 'Como você cria uma lista em Python?',
            options: ['lista = (1, 2, 3)', 'lista = {1, 2, 3}', 'lista = [1, 2, 3]', 'lista = <1, 2, 3>'],
            correctIndex: 2,
            explanation: 'Listas são criadas com colchetes `[]`. Ex: `lista = [1, 2, 3]`.',
        },
        {
            question: 'Como você acessa o PRIMEIRO elemento de uma lista?',
            options: ['lista[1]', 'lista[0]', 'lista.first()', 'lista[-1]'],
            correctIndex: 1,
            explanation: 'Em Python, os índices começam em 0. O primeiro elemento é `lista[0]`.',
        },
        {
            question: 'Qual método adiciona um item ao final de uma lista?',
            options: ['lista.add(item)', 'lista.push(item)', 'lista.append(item)', 'lista.insert(item)'],
            correctIndex: 2,
            explanation: '`lista.append(item)` adiciona um elemento ao final da lista.',
        },
    ],
    '16': [
        {
            question: 'Como você cria um dicionário em Python?',
            options: ['d = [chave: valor]', 'd = (chave: valor)', 'd = {chave: valor}', 'd = <chave: valor>'],
            correctIndex: 2,
            explanation: 'Dicionários usam chaves `{}` com pares `chave: valor`. Ex: `d = {"nome": "Python"}`.',
        },
        {
            question: 'Como você acessa o valor de uma chave em um dicionário?',
            options: ['d.get_value("chave")', 'd["chave"]', 'd.chave', 'get(d, "chave")'],
            correctIndex: 1,
            explanation: 'Para acessar um valor, use a chave entre colchetes: `d["chave"]`. Também é possível usar `d.get("chave")`.',
        },
    ],
    '18': [
        {
            question: 'Qual palavra-chave define uma classe em Python?',
            options: ['object', 'class', 'struct', 'type'],
            correctIndex: 1,
            explanation: 'Classes são definidas com a palavra reservada `class`. Ex: `class MinhaClasse:`.',
        },
        {
            question: 'O que é `__init__` em uma classe Python?',
            options: ['Um método opcional de limpeza', 'O construtor — executado ao criar um objeto', 'Um atributo privado', 'Um método estático padrão'],
            correctIndex: 1,
            explanation: '`__init__` é o método construtor. É chamado automaticamente quando um novo objeto da classe é criado.',
        },
        {
            question: 'O que é `self` em métodos de uma classe?',
            options: ['Uma variável global', 'Referência ao objeto atual (instância)', 'Um parâmetro opcional', 'O nome da classe'],
            correctIndex: 1,
            explanation: '`self` é a referência ao objeto que está chamando o método. Deve ser o primeiro parâmetro de todo método de instância.',
        },
    ],
    '19': [
        {
            question: 'Qual bloco captura exceções em Python?',
            options: ['catch', 'except', 'handle', 'rescue'],
            correctIndex: 1,
            explanation: 'Em Python, usamos `try/except` para capturar e tratar exceções.',
        },
        {
            question: 'O que acontece quando uma exceção não é tratada?',
            options: ['O programa continua normalmente', 'O Python imprime um aviso', 'O programa termina com um Traceback', 'A exceção é ignorada'],
            correctIndex: 2,
            explanation: 'Exceções não tratadas encerram o programa e exibem o Traceback (rastreamento do erro).',
        },
    ],
};

export function loadProgress(): Progress {
    const saved = localStorage.getItem('py-estudos-progress');
    if (saved) return JSON.parse(saved);
    return {
        completedModules: [],
        quizScores: {},
        streak: 0,
        lastVisited: new Date().toISOString(),
        weeklyProgress: [0, 0, 0, 0, 0, 0, 0],
    };
}

export function saveProgress(progress: Progress): void {
    localStorage.setItem('py-estudos-progress', JSON.stringify(progress));
}

export function getModulesWithProgress(progress: Progress): Module[] {
    const nextUnlocked = progress.completedModules.length + 1;
    return MODULES.map(m => ({
        ...m,
        status: progress.completedModules.includes(m.id)
            ? 'completed'
            : m.number === nextUnlocked
                ? 'current'
                : m.number <= nextUnlocked
                    ? 'current'
                    : 'locked',
        quizScore: progress.quizScores[m.id],
    }));
}
