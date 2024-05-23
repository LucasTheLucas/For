tentativas = 1
soma = 0
while tentativas <= 10:
    valor = 0
    valor = float(input(f"{tentativas}.Digite um valor para ser somado: "))
    if valor > 0:
        soma += valor
    else:
        print("Não sera adicionados valores negativos!")
    tentativas += 1

print(soma)