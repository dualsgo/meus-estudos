# CSS Básico
CSS (Cascading Style Sheets) é uma linguagem de estilo utilizada para controlar a apresentação e o layout de documentos HTML. Ele permite definir estilos para elementos individuais ou grupos de elementos, proporcionando controle visual sobre como o conteúdo HTML é exibido em um navegador.

Aqui estão alguns conceitos básicos sobre CSS:

1. Seletores: Os seletores CSS são usados para selecionar elementos HTML aos quais você deseja aplicar estilos. Existem diferentes tipos de seletores, como seletores de elemento, seletores de classe e seletores de ID.

- Seletor de elemento: seleciona elementos HTML com base em seu nome de tag. Por exemplo, o seletor "p" selecionará todos os parágrafos.
- Seletor de classe: seleciona elementos com base no valor do atributo "class". Por exemplo, o seletor ".destaque" selecionará todos os elementos com a classe "destaque".
- Seletor de ID: seleciona um elemento com base no valor do atributo "id". Por exemplo, o seletor "#cabecalho" selecionará o elemento com o ID "cabecalho".

2. Propriedades: As propriedades CSS são usadas para definir os estilos dos elementos selecionados. Cada propriedade tem um valor associado que determina como a propriedade será aplicada. Alguns exemplos de propriedades CSS incluem:

- "color": define a cor do texto.
- "font-size": define o tamanho da fonte.
- "background-color": define a cor de fundo.
- "padding": define o espaçamento interno em torno do conteúdo do elemento.
- "margin": define o espaçamento externo em torno do elemento.

3. Valores: As propriedades CSS são definidas com valores específicos. Alguns exemplos de valores comuns incluem:

- Cores: podem ser especificadas como nomes, como "vermelho" ou "azul", ou usando valores hexadecimais, como "#FF0000" para vermelho.
- Tamanhos: podem ser definidos em pixels (px), porcentagem (%), em (unidades relativas ao tamanho da fonte) ou outras unidades de medida.
- Fontes: podem ser especificadas como nomes de fonte ou famílias de fontes, como "Arial" ou "sans-serif".

4. Estilos em cascata: O termo "cascata" em CSS refere-se à maneira como as regras de estilo são aplicadas quando há conflitos. O CSS segue uma ordem de precedência em que estilos mais específicos têm prioridade sobre estilos mais genéricos. Isso permite que você defina estilos em diferentes níveis, como em um arquivo CSS externo, em um estilo embutido na tag HTML ou diretamente na tag HTML usando o atributo "style".

Essas são apenas algumas noções básicas de CSS. Há muitos outros conceitos e propriedades que você pode explorar para aprimorar seus estilos e layouts de página. É recomendável estudar mais a fundo o CSS para obter um conhecimento mais completo e eficaz na utilização dessa linguagem de estilo.

## Cores

CSS (Cascading Style Sheets) permite especificar cores para elementos em uma página da web. Existem várias formas de definir cores em CSS. Aqui estão algumas das opções mais comuns:

1. Nomes de cores: CSS possui um conjunto pré-definido de nomes de cores que você pode usar diretamente, como "red" (vermelho), "blue" (azul), "green" (verde), "yellow" (amarelo), entre outros. Alguns exemplos:

```css
h1 {
  color: red;
}

p {
  color: blue;
}
```

2. Valores hexadecimais: Outra forma comum de especificar cores em CSS é usando valores hexadecimais. Um valor hexadecimal consiste em uma combinação de números e letras de A a F, representando os componentes de vermelho (R), verde (G) e azul (B) em um formato de três ou seis dígitos. Alguns exemplos:

```css
h1 {
  color: #FF0000; /* vermelho */
}

p {
  color: #0000FF; /* azul */
}
```

3. Valores RGB: A notação RGB (Red, Green, Blue) permite definir a intensidade de cada componente de cor individualmente, variando de 0 a 255. Isso proporciona um controle mais granular sobre as cores. Exemplos:

```css
h1 {
  color: rgb(255, 0, 0); /* vermelho */
}

p {
  color: rgb(0, 0, 255); /* azul */
}
```

4. Valores RGBA: O valor RGBA (Red, Green, Blue, Alpha) é semelhante ao RGB, mas adiciona um quarto valor para controlar a transparência ou opacidade da cor. O valor alfa varia de 0 (totalmente transparente) a 1 (totalmente opaco). Exemplos:

```css
h1 {
  color: rgba(255, 0, 0, 0.5); /* vermelho com 50% de transparência */
}

p {
  color: rgba(0, 0, 255, 0.8); /* azul com 80% de transparência */
}
```

Essas são apenas algumas das maneiras de especificar cores em CSS. Existem outras opções, como valores HSL (Hue, Saturation, Lightness) e HSLA (Hue, Saturation, Lightness, Alpha), que também permitem uma manipulação mais avançada das cores.

### Hex

A notação hexadecimal é uma forma popular de especificar cores em CSS. Ela usa uma combinação de valores numéricos e letras de A a F para representar os componentes de cor vermelha (R), verde (G) e azul (B).

A notação hexadecimal pode ser expressa em um formato de três ou seis dígitos. No formato de três dígitos, cada componente de cor é representado por um único dígito, que é duplicado para corresponder ao formato de seis dígitos. Por exemplo, o valor hexadecimal "#F00" é equivalente a "#FF0000", onde "F0" é expandido para "FF00FF".

A escala numérica varia de 0 a 15 no sistema hexadecimal. Os valores de 0 a 9 correspondem aos dígitos decimais de 0 a 9, enquanto as letras de A a F representam os valores de 10 a 15. Aqui está uma tabela mostrando a correspondência entre os valores hexadecimais e decimais:

```
0 = 0
1 = 1
2 = 2
3 = 3
4 = 4
5 = 5
6 = 6
7 = 7
8 = 8
9 = 9
A = 10
B = 11
C = 12
D = 13
E = 14
F = 15
```

Por exemplo, o valor hexadecimal "#FF0000" representa o vermelho puro, onde o componente de cor vermelha (R) está no seu valor máximo (FF em hexadecimal, que é 255 em decimal) e os componentes verde (G) e azul (B) estão em zero.

Ao usar a notação hexadecimal em CSS, você pode definir cores de fundo, cores de texto, cores de borda e muito mais. Aqui está um exemplo de código CSS usando valores hexadecimais:

```css
h1 {
  color: #FF0000; /* vermelho */
  background-color: #00FF00; /* verde */
  border: 2px solid #0000FF; /* azul */
}
```
## Backgrounds e borders

1. Propriedade `background`:
A propriedade `background` é usada para definir o estilo do plano de fundo de um elemento HTML. Ela permite definir várias propriedades relacionadas ao plano de fundo em uma única declaração. Algumas das propriedades mais comuns incluem:

- `background-color`: Define a cor de fundo do elemento. Você pode usar valores de cor em qualquer formato suportado, como nomes de cores, valores hexadecimais ou valores RGB/RGBA.
Exemplo:
```css
div {
  background-color: yellow;
}
```

- `background-image`: Permite definir uma imagem como plano de fundo do elemento. Você pode especificar a URL da imagem usando a função `url()`.
Exemplo:
```css
div {
  background-image: url('imagem.png');
}
```

- `background-repeat`: Define se a imagem de fundo deve ser repetida ou não. Os valores possíveis são `repeat` (repetir em ambas as direções), `repeat-x` (repetir apenas horizontalmente), `repeat-y` (repetir apenas verticalmente) e `no-repeat` (não repetir).
Exemplo:
```css
div {
  background-repeat: no-repeat;
}
```

Essas são apenas algumas das propriedades disponíveis na propriedade `background`. Há outras propriedades úteis, como `background-size`, `background-position`, entre outras, que permitem um controle mais preciso sobre o estilo de plano de fundo.

2. Propriedade `border`:
A propriedade `border` é usada para definir o estilo das bordas de um elemento HTML. Ela permite definir a espessura, a cor e o estilo da borda. Aqui estão algumas das propriedades relacionadas à borda:

- `border-width`: Define a espessura da borda. Você pode especificar um valor em pixels, em unidades relativas ou usando palavras-chave como `thin`, `medium` e `thick`.
Exemplo:
```css
div {
  border-width: 2px;
}
```

- `border-color`: Define a cor da borda. Assim como na propriedade `background-color`, você pode usar valores de cor em diferentes formatos.
Exemplo:
```css
div {
  border-color: red;
}
```

- `border-style`: Define o estilo da borda, como `solid` (sólida), `dashed` (tracejada), `dotted` (pontilhada), `double` (dupla) e outros.
Exemplo:
```css
div {
  border-style: dashed;
}
```

Você também pode combinar essas propriedades em uma única declaração, utilizando a propriedade `border` seguida pelas três propriedades (width, style, color) separadas por espaços ou barras.
Exemplo:
```css
div {
  border: 2px dashed red;
}
```

Essas são apenas algumas das propriedades relacionadas ao `border`. Há outras propriedades, como `border-radius`, que permite definir bordas arredondadas, e `border-image`, que permite aplicar uma imagem à borda, oferecendo mais opções para estilizar as bordas dos elementos HTML.
## Seletores

Os seletores são uma parte fundamental do CSS, pois permitem selecionar e aplicar estilos a elementos específicos em uma página HTML. Existem vários tipos de seletores disponíveis no CSS. Vou explicar alguns dos seletores mais comumente usados:

1. Seletor de tipo:
O seletor de tipo é usado para selecionar elementos com base em seu tipo HTML. Por exemplo, o seletor `h1` selecionará todos os elementos `h1` (títulos de nível 1) na página.
Exemplo:
```css
h1 {
  color: blue;
}
```

2. Seletor de classe:
O seletor de classe permite selecionar elementos que possuem um determinado valor no atributo `class`. Você pode atribuir a mesma classe a vários elementos e, em seguida, estilizá-los em conjunto usando o seletor de classe.
Exemplo:
```html
<p class="destaque">Este é um parágrafo de destaque.</p>
```
```css
.destaque {
  color: red;
}
```

3. Seletor de ID:
O seletor de ID é usado para selecionar um elemento com base em seu atributo `id`, que deve ser exclusivo na página. O seletor de ID é indicado pelo símbolo `#`.
Exemplo:
```html
<div id="conteudo">Conteúdo principal</div>
```
```css
#conteudo {
  background-color: gray;
}
```

4. Seletor descendente:
O seletor descendente permite selecionar elementos filhos dentro de um elemento pai. Ele usa um espaço para separar os seletores. Por exemplo, o seletor `div p` selecionará todos os elementos `p` que estão dentro de um elemento `div`.
Exemplo:
```css
div p {
  font-size: 16px;
}
```

5. Seletor de atributo:
O seletor de atributo permite selecionar elementos com base em seus atributos e seus valores. Você pode selecionar elementos com um atributo específico, um atributo com um valor específico ou até mesmo um atributo com um valor que corresponda a um padrão específico.
Exemplo:
```css
input[type="text"] {
  border: 1px solid gray;
}
```


6. Seletor de descendente direto:
O seletor de descendente direto é semelhante ao seletor de descendente, mas ele seleciona apenas os elementos filhos diretos de um elemento pai, ignorando os elementos mais profundos na hierarquia.
Exemplo:
```css
div > p {
  color: blue;
}
```
Neste exemplo, apenas os elementos `p` que são filhos diretos de um elemento `div` serão selecionados.

7. Seletor de adjacente:
O seletor de adjacente seleciona um elemento que é adjacente imediato a outro elemento específico. Isso significa que o elemento selecionado deve seguir imediatamente o elemento de referência.
Exemplo:
```css
h1 + p {
  font-weight: bold;
}
```
Neste caso, o seletor `h1 + p` selecionará o elemento `p` que é adjacente imediato a um elemento `h1`.

8. Seletor de pseudo-classe:
Os seletores de pseudo-classe permitem selecionar elementos com base em um estado ou uma ação específica. Por exemplo, a pseudo-classe `:hover` seleciona um elemento quando ele está sendo "hovered" (quando o cursor do mouse está sobre ele).
Exemplo:
```css
a:hover {
  color: red;
}
```
Neste exemplo, os links serão estilizados com a cor vermelha quando o mouse estiver sobre eles.

9. Seletor de pseudo-elemento:
Os seletores de pseudo-elemento são usados para selecionar partes específicas de um elemento e estilizá-las. Eles são representados usando dois sinais de dois pontos `::` antes do nome do pseudo-elemento.
Exemplo:
```css
p::first-line {
  font-weight: bold;
}
```
Neste exemplo, o pseudo-elemento `::first-line` seleciona a primeira linha de cada elemento `p` e aplica a propriedade `font-weight: bold`.

É importante mencionar que os seletores podem ser combinados para formar seletores mais complexos e específicos. Essa combinação permite selecionar elementos de forma precisa e aplicar estilos específicos a eles. A seleção de elementos corretos usando seletores adequados é uma parte essencial do CSS para criar estilos eficientes e controlados em suas páginas da web.

Resumo:

1. `*`: O seletor universal seleciona todos os elementos da página.
2. `#X`: O seletor de identificador seleciona elementos com um identificador específico.
3. `.X`: O seletor de classe seleciona elementos com uma classe específica.
4. `X Y`: O seletor de descendente seleciona elementos Y que são descendentes de elementos X.
5. `X`: O seletor de tipo seleciona elementos com um determinado tipo (tag).
6. `X:visited` e `X:link`: Essas são pseudo-classes que permitem estilizar links visitados e não visitados, respectivamente.
7. `X + Y`: O seletor adjacente seleciona o elemento Y imediatamente após o elemento X.
8. `X > Y`: O seletor de filho seleciona elementos Y que são filhos diretos de elementos X.
9. `X ~ Y`: O seletor de irmão seleciona elementos Y que são irmãos de elementos X.
10. `X[title]`: O seletor de atributo seleciona elementos com um atributo específico.
11. `X[href="foo"]`: O seletor de atributo com valor seleciona elementos com um atributo específico e um valor exato.
12. `X[href*="nettuts"]`: O seletor de atributo com valor parcial seleciona elementos com um atributo específico que contém um valor parcial.
13. `X[href^="http"]`: O seletor de atributo com valor no início seleciona elementos com um atributo específico que começa com um valor específico.
14. `X[href$=".jpg"]`: O seletor de atributo com valor no final seleciona elementos com um atributo específico que termina com um valor específico.
15. `X[data-*="foo"]`: O seletor de atributo de dados seleciona elementos com um atributo de dados específico.
16. `X[foo~="bar"]`: O seletor de atributo com valor de lista seleciona elementos com um atributo específico que contém uma lista de valores separados por espaços.
17. `X:checked`: A pseudo-classe `:checked` seleciona elementos de interface que estão marcados ou selecionados.
18. `X:after`: A pseudo-classe `:after` adiciona conteúdo após o conteúdo de um elemento.

Esses seletores permitem uma grande flexibilidade e controle sobre a estilização de elementos em uma página web. É importante entender como cada um deles funciona para aproveitar ao máximo o CSS em seus projetos.

## Especificidade
A especificidade CSS é um conceito que determina quais regras de estilo devem ser aplicadas a um elemento quando várias regras se aplicam ao mesmo elemento. É uma maneira de resolver conflitos quando diferentes regras têm seletor de destino semelhante.

A especificidade CSS é calculada com base nos seletores usados em cada regra. Cada seletor possui um valor de especificidade atribuído a ele. Quanto maior o valor de especificidade, maior é a prioridade da regra.

Aqui está uma visão geral dos valores de especificidade atribuídos a diferentes seletores:

- Seletor universal (*), seletor combinador (+, >, ~, ' ') e seletor negação (:not) têm um valor de especificidade de 0,0,0,0.
- Seletor de tipo (por exemplo, div, p, span) tem um valor de especificidade de 0,0,0,1.
- Seletor de classe, seletor de atributo e seletor de pseudo-classe têm um valor de especificidade de 0,0,1,0.
- Seletor de ID tem um valor de especificidade de 0,1,0,0.
- Seletor de estilo inline (definido diretamente no elemento usando o atributo style) tem um valor de especificidade de 1,0,0,0.

Quando várias regras se aplicam a um elemento, a regra com a maior especificidade é aplicada. Se duas regras têm a mesma especificidade, a regra que aparece por último no arquivo CSS é aplicada.

Por exemplo, considere as seguintes regras CSS:

```css
p {
  color: red;
}

#myId {
  color: blue;
}

p#myId {
  color: green;
}
```

Nesse caso, se um elemento `<p>` tiver o ID "myId", a cor do texto será verde porque a regra `p#myId` tem uma especificidade maior que as outras duas.

É importante entender a especificidade CSS para evitar conflitos e garantir que as regras de estilo sejam aplicadas corretamente aos elementos desejados.

## Herança

A herança é um conceito importante em CSS que permite que propriedades sejam transmitidas de um elemento pai para seus elementos filhos. Quando uma propriedade é definida em um elemento pai, ela pode ser herdada por seus descendentes, a menos que seja especificamente anulada.

A herança em CSS funciona de acordo com as regras definidas para cada propriedade. Nem todas as propriedades são herdadas por padrão. Algumas propriedades são herdadas e outras não.

Propriedades comuns que são herdadas por padrão incluem:

- `font-family`: especifica a família de fonte a ser usada.
- `font-size`: define o tamanho da fonte.
- `color`: especifica a cor do texto.
- `line-height`: define a altura da linha.
- `text-align`: alinha o texto horizontalmente.
- `font-weight`: define o peso da fonte (por exemplo, negrito ou normal).
- `font-style`: define o estilo da fonte (por exemplo, itálico ou normal).

Por outro lado, algumas propriedades não são herdadas por padrão, como:

- `width`: define a largura do elemento.
- `height`: define a altura do elemento.
- `margin`, `padding`: propriedades relacionadas ao espaçamento ao redor do elemento.
- `border`, `border-radius`: propriedades relacionadas à borda do elemento.
- `background`: define o plano de fundo do elemento.

No entanto, mesmo que uma propriedade não seja herdada por padrão, ela ainda pode ser explicitamente aplicada a um elemento filho e substituir a propriedade herdada do elemento pai.

A herança em CSS pode ser útil para estilizar elementos de forma consistente, especialmente quando se trata de propriedades relacionadas ao texto. No entanto, é importante entender quais propriedades são herdadas e quais não são, para garantir o resultado desejado ao estilizar seus elementos.

## Textos e fontes

Em CSS, existem várias propriedades relacionadas a textos e fontes que podem ser utilizadas para estilizar o texto em um documento HTML. Aqui estão algumas das propriedades mais comuns:

1. `font-family`: Define a família de fonte a ser usada para o texto. É possível especificar várias opções de fonte em ordem de preferência, separadas por vírgula. Exemplo: `font-family: Arial, sans-serif;`

2. `font-size`: Define o tamanho da fonte. Pode ser especificado em unidades absolutas (como pixels) ou relativas (como em ou porcentagem). Exemplo: `font-size: 16px;`

3. `font-weight`: Define o peso da fonte. Pode ser usado para deixar o texto em negrito. Exemplo: `font-weight: bold;`

4. `font-style`: Define o estilo da fonte. Pode ser usado para deixar o texto em itálico. Exemplo: `font-style: italic;`

5. `text-align`: Alinha o texto horizontalmente dentro de seu contêiner. Exemplos: `text-align: left;`, `text-align: center;`, `text-align: right;`

6. `text-decoration`: Adiciona uma decoração ao texto, como sublinhado ou linha através do texto. Exemplos: `text-decoration: underline;`, `text-decoration: line-through;`

7. `text-transform`: Transforma o texto em maiúsculas ou minúsculas. Exemplos: `text-transform: uppercase;`, `text-transform: lowercase;`

8. `color`: Define a cor do texto. Pode ser especificado usando nomes de cores, códigos hexadecimais ou valores RGB. Exemplos: `color: red;`, `color: #336699;`, `color: rgb(255, 0, 0);`

Essas são apenas algumas das propriedades CSS que podem ser utilizadas para estilizar textos e fontes. Existem muitas outras propriedades disponíveis que permitem um controle mais refinado sobre a aparência do texto em um documento HTML.
