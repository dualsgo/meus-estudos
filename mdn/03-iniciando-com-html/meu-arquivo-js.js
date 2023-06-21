const list = document.createElement('ul');
const info = document.createElement('p');
const html = document.querySelector('html');

info.textContent = 'Below is a dynamic list. Click anywhere on the page to add a new list item. Click an existing list item to change its text to something else.';

document.body.appendChild(info);
document.body.appendChild(list);

html.onclick = function() {
  const listItem = document.createElement('li');
  const listContent = prompt('What content do you want the list item to have?');
  listItem.textContent = listContent;
  list.appendChild(listItem);

  listItem.onclick = function(e) {
    e.stopPropagation();
    const listContent = prompt('Enter new content for your list item');
    this.textContent = listContent;
  }
}

// O JavaScript adicionou uma lista vazia à página. Agora, quando você clica em qualquer lugar da lista, uma caixa de diálogo aparecerá pedindo para que você, insira algum texto para um novo item de lista. Quando você pressiona o botão OK, um novo item será adicionado à lista contendo o texto. Quando você clica em um item de lista existente, uma caixa de diálogo será exibida permitindo que você altere o texto do item.