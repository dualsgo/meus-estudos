const myImage = document.querySelector("img"); // Selecionamos o elemento img e o armazenamos na variável myImage

myImage.onclick = () => { // () => é uma função de seta atribuída à propriedade onclick do elemento myImage (img). Isso significa que quando o elemento myImage (img) for clicado, a função será executada
    const mySrc = myImage.getAttribute("src"); // Armazenamos o valor do atributo src do elemento myImage (img) na variável mySrc
    if (mySrc === "imagens/firefox-icon.png") { // Verificamos se o valor da variável mySrc é igual a "images/firefox-icon.png"
        myImage.setAttribute("src", "imagens/firefox2.png"); // Se for, alteramos o valor do atributo src para "images/firefox2.png"
    } else { // Caso contrário
        myImage.setAttribute("src", "imagens/firefox-icon.png"); // Alteramos o valor do atributo src para "images/firefox-icon.png"
    }
};

// O código recupera o valor do atributo src da imagem.
// O código usa uma condicional para verificar se o valor src é igual ao caminho da imagem original:
// Se for, o código altera o valor src para o caminho da segunda imagem, forçando a outra imagem a ser carregada dentro do elemento <img>.
// Se não for (o que significa que já deve ter mudado), o valor src volta para o caminho da imagem original, para o estado original.


let myButton = document.querySelector("button"); // Selecionamos o elemento button e o armazenamos na variável myButton
let myHeading = document.querySelector("h1"); // Selecionamos o elemento h1 e o armazenamos na variável myHeading

function setUserName() { // Criamos uma função chamada setUserName
    const myName = prompt("Por favor digite o seu nome."); // A função prompt() exibe uma caixa de diálogo que solicita ao usuário a entrada de dados. O valor que o usuário insere é armazenado na variável myName
    if (!myName) { // Verificamos se a variável myName não contém um valor. A Expressão lógica ! (não) verifica se o valor de uma variável é falso. Nesse caso, verifica se myName é nulo por meio do valor booleano false. Isso ocorre porque o método prompt() retorna o valor nulo se o usuário clicar no botão Cancelar da caixa de diálogo
        setUserName(); // Se não contiver, chamamos a função setUserName() novamente para que o usuário insira um valor
    } else { // Caso contrário, se contiver um valor
        localStorage.setItem("name", myName); // Chamamos o método setItem() do objeto localStorage, que permite que nós armazenemos dados no navegador e os recuperemos posteriormente. Os dados são armazenados permanentemente, mesmo após o navegador ser fechado e reaberto nos parametros "name" e myName que significam que o nome do item é "name" e o valor é a variável myName. Isso cria uma espécie de arquivo de armazenamento chave-valor no navegador que pode ser usado para armazenar dados no futuro. Se quiser alterar o valor de um dado armazenado, basta chamar o método setItem() novamente com o mesmo nome da chave. Como o localStorage é específico para o domínio, todos os sites armazenam dados separadamente.
        myHeading.textContent = `Mozilla é legal, ${myName}`; // Alteramos o valor da propriedade textContent do elemento myHeading para "Mozilla é legal, " concatenado com o valor da variável myName
    }
}

myButton.onclick = () => {
    setUserName();
}; // Criamos uma função anônima atribuída à propriedade onclick do elemento myButton (button). Isso significa que quando o elemento myButton (button) for clicado, a função será executada. A função chama a função setUserName() definida anteriormente e executa o código dentro dela. Com isso, o usuário pode alterar o nome que é armazenado no navegador