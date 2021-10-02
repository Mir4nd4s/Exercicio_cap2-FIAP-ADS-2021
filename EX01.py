print("*(considere sua altura em metros [ex: 1.68] e seu peso em Kg)*\nOlá Usúario!")
peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / altura ** 2
print("Seu IMC é {:.2f}".format(imc))


if imc < 16.00:
    print("Avaliação do seu IMC é: BAIXO PESO GRAU III")
elif imc <= 16.99:
    print("Avaliação do seu IMC é: BAIXO PESO GRAU II")
elif imc <= 18.49:
    print("Avaliação do seu IMC é: BAIXO PESO GRAU II")
elif imc <= 24.99:
    print("Avaliação do seu IMC é: PESO IDEAL")
elif imc <= 29.99:
    print("Avaliação do seu IMC é: SOBREPESO")
elif imc <= 34.99:
    print("Avaliação do seu IMC é: OBESIDADE GRAU I")
elif imc <= 39.99:
    print("Avaliação do seu IMC é: OBESIDADE GRAU II")
if imc > 40:
    print("Avaliação do seu IMC é: OBESIDADE GRAU III")


