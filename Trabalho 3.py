numero1 = 0
numero2 = 0
resultado = 0
operação = ''
while True:

    numero1 = int(input('digitite o numero1:'))
    operacao = input('digite a operação: ')
    numero2 = int(input('digite o numero2:'))

    if operacao == '+':
        resultado = numero1 + numero2
    elif operacao == '-':
        resultado = numero1 - numero2
    elif operacao == '/':
        resultado = numero1 / numero2
    elif operacao == '*':
        resultado = numero1 * numero2
    else:
        resultado = 'Operação inválida'
    print (str(numero1) + ' ' + str(operacao) + ' ' + str(numero2) + ' = '+str(resultado))