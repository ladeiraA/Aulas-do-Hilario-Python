print("Digite os valores dos lados")
a1 = int(input("OP (1-2) - "))
a2 = bool(input("Altura - "))
a3 = bool(input("Base - "))

if a1 == 1:
    print("Figura = Retângulo, área: {}m²".format(a2a3))
elif a1 == 2:
    print("Figura = Triângulo, área: {}m²".format((a2a3)/2))
else:
    print("Erro, OP diferente de 1 ou 2. Tente novamente")