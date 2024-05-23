salario = 2000
p_aumento = 2000*0.015
ano_contratado = 1995
ano_atual = 2024
salario_do_ano = 0

anos_trabalhados = ano_atual - ano_contratado

for i in range(anos_trabalhados+1):
    salario_do_ano = salario + p_aumento * i
    print(f"O Salario em {ano_contratado + i} foi de: {salario_do_ano}")


