##Ej 1.2
c="micamaesroja1"
while True:
    ingreso=input("Ingrese la contraseña: ")
    if ingreso==c:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta, intenta de nuevo")