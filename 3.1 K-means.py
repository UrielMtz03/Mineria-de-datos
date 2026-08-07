#3.1
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
df=pd.read_csv("dataset_clientes.csv")
x=df[["Sucursal", "Gasto_Mensual_MXN", "Compras_Mensuales"]]

x=x.dropna()
x=pd.get_dummies(x, columns=["Sucursal"], drop_first=True)
escalador = StandardScaler()
x_escalado = escalador.fit_transform(x)

modelo = KMeans(n_clusters=3, random_state=42, n_init=10)
clusters = modelo.fit_predict(x_escalado)

df_limpio = x.copy()
df_limpio["Cluster"] = clusters

print(df_limpio)
print(df_limpio.groupby("Cluster").mean())