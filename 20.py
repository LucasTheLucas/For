numero = 0
quantidade_de_vezes = 0
numero_de_pares = 0
numero_de_impares = 0
primeira_vez = True
texto = ""

while numero != 1000:
    numero = int(input("Digite um número para ser avaliado: "))
    quantidade_de_vezes += 1

    if(numero % 2 == 0):
        numero_de_pares += 1
        if(primeira_vez):
            primeira_vez = False
            texto = (texto + f"{numero} é par")
        
        else:
            texto = (texto + f", {numero} é par")

    else:
        numero_de_impares += 1
        if(primeira_vez):
            primeira_vez = False
            texto = (texto +f"{numero} é impar")

        else:
            texto = (texto + f", {numero} é impar")

print(f"[{texto}]\nVocê digitou {quantidade_de_vezes} números:\nPares [{numero_de_pares}]\nImpares [{numero_de_impares}]")

