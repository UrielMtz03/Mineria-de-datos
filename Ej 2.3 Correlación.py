#Ej 3 Correlación
import pandas as pd
datos = pd.read_csv("estudiantes.csv")

variables = [
    "Asistencia",
    "Tareas",
    "Examen",
    "Calificacion_Final",
    "Horas_Estudio"
]
correlacion = datos[variables].corr()

print("Matriz de correlación")
print(correlacion)