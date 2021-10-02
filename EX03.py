v1 = int(input("Digite a quantidade de votos para Segunda-feira: "));
v2 = int(input("Digite a quantidade de votos para Terça-feira: "));
v3 = int(input("Digite a quantidade de votos para Quarta-feira: "));
v4 = int(input("Digite a quantidade de votos para Quinta-feira: "));
v5 = int(input("Digite a quantidade de votos para Sexta-feira: "));

maior = v1

if v2 > maior:
    maior = v2
if v3 > maior:
    maior = v3
if v4 > maior:
    maior = v4
if v5 > maior:
    maior = v5

dia = ""

if maior == v1:
    dia = "Segunda-feira"
if maior == v2:
    dia == "Terça-feira"
if maior == v3:
    dia = "Quarta-feira"
if maior == v4:
    dia = "Quinta-feira"
if maior == v5:
    dia = "Sexta-feira"

print("O dia da semana escolhido foi, {} com {} votos".format(dia,maior))