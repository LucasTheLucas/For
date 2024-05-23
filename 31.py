saque = int(input("Digite o valor do saque: "))
nota_200 = 0
nota_100 = 0
nota_50 = 0
nota_20 = 0
nota_10 = 0
nota_5 = 0
nota_2 = 0
nota_1 = 0

while saque > 0:
    if(saque > 199):
        nota_200 = saque // 200
        saque -= 200 * nota_200

    elif(saque > 99):
        nota_100 = saque // 100
        saque -= 100 * nota_100

    elif(saque > 49):
        nota_50 = saque // 50
        saque -= 50 * nota_50

    elif(saque > 19):
        nota_20 = saque // 20
        saque -= 20 * nota_20

    elif(saque > 9):
        nota_10 = saque // 10
        saque -= 10 * nota_10

    elif(saque > 4):
        nota_5 = saque // 5
        saque -= 5 * nota_5

    elif(saque > 1):
        nota_2 = saque // 2
        saque -= 2 * nota_2

    else:
        nota_1 = saque
        saque - nota_1

print(f"200[{nota_200}], 100[{nota_100}], 50[{nota_50}], 20[{nota_20}], 10[{nota_10}], 5[{nota_5}], 2[{nota_2}], 1[{nota_1}]")
    