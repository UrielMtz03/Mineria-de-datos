import csv
total=0
with open("ventas.csv", "r") as archivo:
    lector=csv.DictReader(archivo)

    for fila in lector:
        cantidad=int(fila["Cantidad"])
        precio=float(fila["Precio_Unitario"])
        total+=cantidad*precio
print("Ventas totales:", total)