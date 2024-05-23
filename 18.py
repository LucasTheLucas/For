quantos_numeros = int(input("Digite quantos número vão ser lidos: "))
maior = 0
menor = 0

for i in range (0,quantos_numeros):
    valor = int(input("Digite um número: "))
    if(valor >=  maior):
        maior = valor
    if(valor <=  menor):
        menor = valor

print(f"O maior número foi {maior} e o menor foi {menor}")
    