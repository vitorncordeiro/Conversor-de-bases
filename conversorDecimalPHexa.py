decimalUsuario = int(input('Digite o número decimal: '))
dividendo = decimalUsuario
listaHexa = []
listaLETRAS = ['A', 10, 'B', 11, 'C', 12, 'D', 13, 'E', 14, 'F', 15]

while dividendo > 0:
    if dividendo <= 16:
        listaHexa.append(dividendo)
        break
    quosciente = dividendo // 16
    resto = dividendo % 16
    listaHexa.append(resto)
    dividendo = quosciente
for posicao, valor in enumerate(listaHexa):
   if valor in listaLETRAS:
       listaHexa[posicao] = listaLETRAS[listaLETRAS.index(valor) - 1]
hexaFinal = []
for x in listaHexa:
    hexaFinal.append(str(x))
hexaFinalFormatado = ''.join(hexaFinal)[::-1]
print(hexaFinalFormatado)