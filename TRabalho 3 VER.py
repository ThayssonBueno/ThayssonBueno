print("Digite um numero")
numero1 = int(input() )

print("digite um operador")
operador = input()

print("Digite um segundo numero")
numero2 = int(input())

if operador == '+':
    resultado = numero1 + numero2
    print(resultado)
elif operador == "-":
    resultado = numero1 - numero2
    print(resultado)
elif operador == '*':
    resultado = numero1 * numero2
    print(resultado)
elif operador == '/':
    resultado = numero1 / numero2
    print(resultado)
else:
    print("Operador incorreto")
    