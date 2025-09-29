import numpy as np
import random
import matplotlib.pyplot as plt 

np.random.seed(42)
random.seed(42)
N = 1000 

num_ensayos = 10
prob_exito = 0.3
var_binomial = np.random.binomial(n=num_ensayos, p=prob_exito, size=N)

print(f"1. Binomial (primeros 10 valores): {var_binomial[:10]}")

plt.figure(figsize=(6, 4))
plt.hist(var_binomial, bins=np.arange(num_ensayos + 2) - 0.5, rwidth=0.8, color='skyblue')
plt.title('Distribución Binomial (n=10, p=0.3)')
plt.xticks(np.arange(num_ensayos + 1))
plt.xlabel('Número de Éxitos')
plt.ylabel('Frecuencia')
plt.grid(axis='y', alpha=0.5)
plt.show()


tasa_media = 4.0
var_poisson = np.random.poisson(lam=tasa_media, size=N)

print(f"\n2. Poisson (primeros 10 valores): {var_poisson[:10]}")


plt.figure(figsize=(6, 4))
plt.hist(var_poisson, bins=np.arange(max(var_poisson) + 2) - 0.5, rwidth=0.8, color='lightgreen')
plt.title(f'Distribución de Poisson (λ={tasa_media})')
plt.xticks(np.arange(max(var_poisson) + 1))
plt.xlabel('Número de Eventos')
plt.ylabel('Frecuencia')
plt.grid(axis='y', alpha=0.5)
plt.show()

resultados_dado = [1, 2, 3, 4, 5, 6]
num_lanzamientos = 20
simulacion_dado = random.choices(resultados_dado, k=num_lanzamientos)

print(f"\n3. Simulación de un Dado (20 lanzamientos): {simulacion_dado}")

baraja = ['A', '2', '3', '4', 'J', 'Q', 'K']
muestreo_sin_reemplazo = random.sample(baraja, k=3)

print(f"4. Muestreo Sin Reemplazo (3 cartas): {muestreo_sin_reemplazo}")