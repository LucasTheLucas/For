numero = int(input("Digite um número e vamos descobrir seus divisores: "))
texto = (f"Numeros que podem dividir {numero}: ")
for i in range(1,numero+1):
    if(numero % i == 0):
        texto += (f"[{i}]")

print(texto)