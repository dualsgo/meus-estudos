import qrcode

endereço = "https://www.google.com.br"
imagem = qrcode.make(endereço)
imagem.save('qrcode.png', 'PNG')