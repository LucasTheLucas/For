sal_Carlos = float(input("Digite o salaria de Carlos: "))
sal_Joao = sal_Carlos/3

ban_Carlos = 0
ban_Joao = 0

meses = 0

while ban_Carlos > ban_Joao or meses == 0:
    meses += 1

    ban_Joao += sal_Joao
    ban_Joao += ban_Joao*0.05

    ban_Carlos += sal_Carlos
    ban_Carlos += ban_Joao*0.02 

print(f"Quantidade de meses[{meses}]\nRenda de João no banco[{ban_Joao}]\nRenda de Carlos no banco[{ban_Carlos}]")