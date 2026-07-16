#Ej 4 Gráficas
import pandas as pd
import matplotlib.pyplot as plt
datos = pd.read_csv("estudiantes.csv")

# Gráfica de barras
plt.figure(figsize=(8,5))
plt.bar(datos["Nombre"], datos["Calificacion_Final"])
plt.title("Calificación final por estudiante")
plt.xlabel("Estudiantes")
plt.ylabel("Calificación")
plt.xticks(rotation=45)
plt.show()

# Histograma
plt.figure(figsize=(8,5))
plt.hist(datos["Calificacion_Final"], bins=5)
plt.title("Histograma de Calificaciones")
plt.xlabel("Calificación")
plt.ylabel("Frecuencia")
plt.show()

# Gráfica de dispersión
plt.figure(figsize=(8,5))
plt.scatter(datos["Horas_Estudio"], datos["Calificacion_Final"])
plt.title("Horas de estudio vs Calificación Final")
plt.xlabel("Horas de estudio")
plt.ylabel("Calificación Final")
plt.show()