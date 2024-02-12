a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente C: "))

delta = (b ** 2) - 4*a*c

if delta < 0 :
    print("Não existe raiz real")
elif delta == 0:
    x1 = (-b + delta ** 0.5) / (2*a)
    print("Raiz: ",x1)
else :
    x1 = (-b + delta ** 0.5) / (2*a)
    x2 = (-b - delta ** 0.5) / (2*a)
    print("Primeira raiz: ",x1)
    print("Segunda raiz: ",x2 )
