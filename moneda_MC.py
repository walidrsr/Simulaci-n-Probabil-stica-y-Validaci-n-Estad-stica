import pandas as pd
import numpy as np
import random 
import matplotlib.pyplot as plt

cantidad_de_tiras_moneda = 10000
numero_de_experimentos = 1000

simulacion = np.random.randint(0,2,size=(numero_de_experimentos,cantidad_de_tiras_moneda)) # 10mil lanzamientos , 1mil experimetos / simulaciones
conteo = np.sum(simulacion,axis=1) # por cada experimento cuento los 1 que son las caras
conteo:list = conteo

#print(simulacion)
#print(conteo)

df =pd.DataFrame({
    'cantidad_de_caras' : conteo
}) #los convierto a dataframe para poder manipular mejor los datos



desvio = df.std()
#media = df.mean()
#moda = df.mode()




# Graficamos la distribucion de los datos
plt.figure(figsize=(8, 5))
plt.hist(conteo, bins=17, color='lightgreen', edgecolor='black', alpha=1)

plt.title('Histograma de frecuencia de caras')
plt.xlabel('Cantidad de Caras')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()


cantidad = 0 #contador de cantidad donde hay mas de 5200 caras
 
for i in range(len(conteo)):  # Aca recorro toda la lista y los que son mayores a 5200 le sumo uno a cantidad
   if conteo [i] >= 5200:
        cantidad += 1

probabilidad =  (cantidad / numero_de_experimentos ) * 100# Determino la probabilidad de que las "caras" salgan mas de 5200 veces
print(f'la probabilidad de que salgan mas de 5200 caras es : {probabilidad}%')













    
     