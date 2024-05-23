#5. Faça um programa que peça ao usuário digitar 10 valores e some-os;
i = 0
soma = 0
while i < 10:
    soma += float(input(f"{i+1} Digite um valor: "))
    i += 1
print(f"A soma desses valores é de: {soma}")