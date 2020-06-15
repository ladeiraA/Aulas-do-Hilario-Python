print("Seletor de triangulos")
a = int(input("Lado 1 = "))
b = int(input("Lado 2 = "))
c = int(input("Lado 3 = "))
#if (b+c<a)and(c+a<b)and(b+a<c):
    if (a==b==c):
        print("Triângulo Equilátero")
    elif ((a==b)or(b==c)or(a==c)):
        print("Triângulo Isóceles")
    else:
        print("Triângulo Escaleno")
#else:
#   print("Erro, a soma de dois lados não pode ser menor que o valor do outro")