listaDecimal = []

base = 2
binarioUsuario = input('Digite o número em binário: ')[::-1] # invertendo o número, se for 100 fica 001
for posicao, i in enumerate(binarioUsuario):#retorna o valor e a posição do i
    simbolo = int(i)
    contaConversao = simbolo*(base**posicao)#faz a operação pra converter
    listaDecimal.append(contaConversao)
DecimalFinal = sum(listaDecimal)
print(DecimalFinal)
