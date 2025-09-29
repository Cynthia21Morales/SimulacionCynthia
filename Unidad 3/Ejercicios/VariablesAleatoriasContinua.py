import numpy as np
import matplotlib.pyplot as plt 

np.random.seed(123)
N = 10000 
media = 75
desviacion_estandar = 8
var_normal = np.random.normal(loc=media, scale=desviacion_estandar, size=N)

print(f"1. Normal (primeros 5 valores): {var_normal[:5]}")

plt.figure(figsize=(6, 4))
plt.hist(var_normal, bins=50, density=True, alpha=0.7, color='lightcoral')
plt.title('Distribución Normal')
plt.xlabel('Valores')
plt.ylabel('Densidad')
plt.grid(axis='y', alpha=0.5)
plt.show()

limite_inf = 5.0
limite_sup = 15.0
var_uniforme = np.random.uniform(low=limite_inf, high=limite_sup, size=N)

print(f"\n2. Uniforme (primeros 5 valores): {var_uniforme[:5]}")

plt.figure(figsize=(6, 4))
plt.hist(var_uniforme, bins=50, density=True, alpha=0.7, color='skyblue')
plt.title('Distribución Uniforme')
plt.xlabel('Valores')
plt.ylabel('Densidad')
plt.grid(axis='y', alpha=0.5)
plt.show()

tasa_lambda = 0.1 
var_exponencial = np.random.exponential(scale=1/tasa_lambda, size=N)

print(f"\n3. Exponencial (primeros 5 valores): {var_exponencial[:5]}")


plt.figure(figsize=(6, 4))
plt.hist(var_exponencial, bins=50, density=True, alpha=0.7, color='lightgreen')
plt.title('Distribución Exponencial')
plt.xlabel('Valores')
plt.ylabel('Densidad')
plt.grid(axis='y', alpha=0.5)
plt.show()
