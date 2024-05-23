contador = 0
soma = 0
notasvalidas = True

while notasvalidas:
    nota = int(input("Digite sua nota entre 10 e 20: "))
    if(10 <= nota <= 20):
        soma += nota
        contador += 1
    
    else: 
        notasvalidas = False

print(f"A media é de {soma/contador}")