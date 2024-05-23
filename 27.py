
varA = 1
varB = 0
varC = 0

while varC <= 4000000:
    varC = varA + varB
    varA = varB
    varB = varC
    if(varC % 2 == 0):
        print(varC)
