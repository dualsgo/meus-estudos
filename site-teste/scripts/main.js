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


function setUserName() { // Criamos uma função chamada setUserName()
    let myName = prompt('Entre com o seu nome.'); // A função usa a função prompt() para solicitar ao usuário que insira um nome. O valor do nome é armazenado na variável myName por meio da função prompt()
    if(!myName) { // A função verifica se o nome é nulo. Se for, a função setUserName() é executada novamente. Isso ocorre se o usuário clicar em Cancelar.
      setUserName(); // Se o nome não for nulo, a função setUserName() usa a função setItem() do objeto localStorage para criar um item chamado 'name' e definir seu valor como o nome inserido pelo usuário por meio da função prompt()
    } else { // Caso contrário
      localStorage.setItem('name', myName); // A função setUserName() define o valor do cabeçalho h1 para uma string, mais o nome definido pelo usuário por meio da função prompt()
      myHeading.innerHTML = 'Mozilla is cool, ' + myName;  // myHeading é o elemento h1 que criamos anteriormente. A propriedade innerHTML define o conteúdo HTML de qualquer elemento. Aqui, estamos definindo-o como uma string composta da frase 'Mozilla is cool, ' e do nome definido pelo usuário.
    } 
  }
  
  if(!localStorage.getItem('name')) { // A função verifica se já existe um item 'name' definido:
    setUserName(); // Se não existir, a função setUserName() é executada para criar o item e definir o nome do usuário.
  } else { // Caso contrário
    let storedName = localStorage.getItem('name'); // Se já existir, a função getItem() do objeto localStorage recupera o item 'name' e o armazena na variável storedName
    myHeading.innerHTML = 'Mozilla is cool, ' + storedName; // De novo, myHeading é o elemento h1 que criamos anteriormente. A propriedade innerHTML define o conteúdo HTML de qualquer elemento. Aqui, estamos definindo-o como uma string composta da frase 'Mozilla is cool, ' e do nome definido pelo usuário.
  }
myButton.onclick = () => { // () => é uma função de seta atribuída à propriedade onclick do elemento myButton (button). Isso significa que quando o elemento myButton (button) for clicado, a função será executada
    setUserName(); // A função setUserName() é executada
};

//Vimos como usar o JavaScript para alterar o conteúdo HTML de um elemento <h1> quando o usuário clica em um botão, solicitando que ele insira um novo nome e armazenando esse nome no armazenamento local do navegador, para que ele possa ser recuperado e usado posteriormente. Também vimos como usar a API do localStorage para armazenar dados no navegador, recuperá-los posteriormente e verificar se os dados já existem.