decimalDoUsuario = int(input('Insira o número decimal que será convertido para binário: '))
novoDecimal = decimalDoUsuario
baseBinario = 2
listaBinario = []
while novoDecimal >= 1:
    if novoDecimal == 1:
        listaBinario.insert(0, novoDecimal)
        break
    quoscienteDecimal = novoDecimal // 2
    restoDecimal = novoDecimal % 2
    listaBinario.insert(0, restoDecimal)
    novoDecimal = quoscienteDecimal
binarioFinal = []
for i in listaBinario:
    binarioFinal.append(str(i))
binarioFinalFormatado = ''.join(binarioFinal)
print(binarioFinalFormatado)


#Aqui da pra testar se o valor que deu tua conta é igual ao valor que o algoritmo calculou


resultadoContaUsuario = input('Digite o resultado que você obteve com sua conta: ')
if binarioFinalFormatado == resultadoContaUsuario:
    print('Você calculou corretamente!')
else:
    print('Você errou.')

