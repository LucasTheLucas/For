numero = int(input("Digite um número e vamos somar seus divisores: "))
soma_divisores = 0

for i in range(1,numero):
    if(numero % i == 0):
        soma_divisores += i

print(soma_divisores)