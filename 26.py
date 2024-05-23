numero = int(input("Digite um número: "))
continua = True

while continua:
    if(numero % 11 == 0 or numero % 13 == 0 or numero % 17 == 0):
        continua = False

    else:
        numero += 1

print(numero)