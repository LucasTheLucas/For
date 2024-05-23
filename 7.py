menor_numero = 0
maior_numero = 0
tentativa = 0
while tentativa < 10:
    valor = float(input(f"{tentativa+1}.Digite um valor: "))
    if valor >= maior_numero:
        maior_numero = valor
    if (valor <= menor_numero):
        menor_numero = valor
    tentativa += 1

print(f"O maior número foi {maior_numero} e o menor foi {menor_numero}")
            