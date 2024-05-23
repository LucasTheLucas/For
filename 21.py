inicio = int(input("Digite um valor: "))
final = int(input("Digite um valor maior que o anterior: "))
soma = 0
multiplicado = 1

for inicio in range(final+1):
    if(inicio % 2 == 0):
        soma += inicio
    
    else:
        multiplicado = multiplicado * inicio

print(f"Todos os pares somados: {soma}\nTodos os impares multiplicados: {multiplicado}")