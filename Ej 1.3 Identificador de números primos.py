##Ej 1.3
n=int(input("Ingrese un número entero: "))
if n<=1:
    print("No es un número primo")
else:
    pr=True
    for i in range(2, n):
        if n%i==0:
            pr=False
            break
    if pr:
        print("Es un número primo")
    else:
        print("No es un número primo")