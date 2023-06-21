const myHeading = document.querySelector("h1"); // Criamos uma constante chamada myHeading e atribulimos a ela o elemento h1 por meio da função querySelector()
myHeading.textContent = "Olá mundo!"; // Alteramos o texto do elemento h1 por meio da propriedade textContent

let myVariable; // Criamos uma variável chamada myVariable
myVariable = "Bob"; // Atribuimos o valor "Bob" a variável myVariable
myVariable; // Retorna "Bob"
myVariable = "Steve"; // Alteramos o valor da variável myVariable para "Steve"
myVariable; // Retorna "Steve"

// string - texto
// number - número
// boolean - true ou false
// null - valor nulo
// undefined - valor indefinido
// symbol - valor único

//Você pode escrever comentários em JavaScript da mesma forma que em CSS:

/*
Tudo no meio é um comentário.
*/

// Se o seu comentário não contém quebras de linha, é uma opção colocá-lo atrás de duas barras como esta:

// Isso é um comentário


// Operadores - Um operador é um símbolo que realiza uma operação matemática ou lógica com um ou dois valores ou variáveis.

// Operadores aritméticos
// + Adição
// - Subtração
// * Multiplicação
// / Divisão
// % Resto da divisão
// ++ Incremento

// Operadores de atribuição
// = Atribuição
// += Atribuição de adição
// -= Atribuição de subtração
// *= Atribuição de multiplicação
// /= Atribuição de divisão
// %= Atribuição de resto da divisão

// Operadores de comparação
// == Igual a
// === Igual a e do mesmo tipo
// != Diferente de
// !== Diferente de e do mesmo tipo
// > Maior que
// < Menor que
// >= Maior ou igual a

// Operadores lógicos
// && E
// || Ou
// ! Não

// Operadores de string
// + Concatenação

// Operadores ternários
// ? : Operador ternário

// Operadores de incremento e decremento
// ++ Incremento
// -- Decremento

let iceCream = "chocolate"; // Criamos uma variável chamada iceCream e atribuimos a ela o valor "chocolate"
if (iceCream === "chocolate") {
  alert("Sim, eu amo sorvete de chocolate!"); // Se o valor da variável iceCream for igual a "chocolate", a condição if é satisfeita e exibe um alert
} else {
  alert("Aaaah, mas chocolate é o meu favorito…"); // Se o valor da variável iceCream não for igual a "chocolate", a condição if não é satisfeita e exibe um alert
}

function multiply(num1, num2) { // Criamos uma função chamada multiply que recebe dois parâmetros: num1 e num2
    let result = num1 * num2; // Criamos uma variável chamada result e atribuimos a ela o valor da multiplicação de num1 e num2
    return result; // Retornamos o valor da variável result
  }

multiply(1,2)

document.querySelector("html").addEventListener("click", function () { // Selecionamos o elemento html e adicionamos um evento de clique a ele
    alert("Ai! Pare de me cutucar!"); // Exibimos um alerta quando o evento de clique é acionado
  }); // Fechamos a função


  document.querySelector("html").addEventListener("click", () => { // () => é uma função de seta
    alert("Ai! Pare de me cutucar!");
  });