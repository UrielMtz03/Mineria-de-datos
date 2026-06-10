import csv
promedios=[]
aprobados=0
reprobados=0
with open("calificaciones.csv", "r") as archivo:
    lector=csv.DictReader(archivo)
    for fila in lector:
        nombre=fila["Nombre"]
        p1=float(fila["Parcial1"])
        p2=float(fila["Parcial2"])
        p3=float(fila["Parcial3"])
        promedio=(p1+p2+p3)/3
        promedios.append({
            "nombre":nombre,
            "promedio":promedio
        })
        print(f"{nombre}:{promedio:.2f}")
        if promedio>=60:
            aprobados+=1
        else:
            reprobados+=1
promedio_general=sum(alumno["promedio"] for alumno in promedios)/len(promedios)
mejor=max(promedios, key=lambda x:x["promedio"])
peor=min(promedios, key=lambda x:x["promedio"])
print("~~~RESULTADOS~~~")
print(f"Promedio general:{promedio_general:.2f}")
print(f"Mejor promedio:{mejor['nombre']} ({mejor['promedio']:.2f})")
print(f"Peor promedio:{peor['nombre']} ({peor['promedio']:.2f})")
print(f"Aprobados:{aprobados}")
print(f"Reprobados:{reprobados}")