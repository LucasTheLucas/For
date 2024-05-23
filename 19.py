numero = int(input("Digite um número entre 100 e 999: "))
ioo = 0
oio = 0 
ooi = 0

ioo = numero // 100
oio = (numero % 100) // 10
ooi = numero % 10

print(f"{ioo}, {oio} e {ooi}")

#######################################################

Numero = int(input("Digite um número de 100 a 999: "))
if(Numero >= 100 and Numero <= 999):
    String_Numero = str(Numero)

    for algarismo in range(len(String_Numero)):
        print(String_Numero[algarismo])
