nome = input("Nome do cliente: ")
faturamento = float(input("Digite o faturamento anual de {}: ".format(nome)))
plano = input("Digite o tipo da assinatura: ")

if plano.upper() == "BASIC":
    bonus = float(faturamento * 0.3)
    print("{}, deve pagar: {} R$".format(nome,bonus))
elif plano.upper() == "SILVER":
    bonus = float(faturamento * 0.2)
    print("{}, deve pagar: {} R$".format(nome,bonus))
elif plano.upper() == "GOLD":
    bonus = float(faturamento * 0.1)
    print("{}, deve pagar: {} R$".format(nome,bonus))
elif plano.upper() == "PLATINUM":
    bonus = float(faturamento * 0.05)
    print("{}, deve pagar: {} R$".format(nome,bonus))
else:
    print("Assinatura inválida... Tente novamente!")


