import numpy as np
import matplotlib.pyplot as plt

np.random.seed(303)

N = 10000        
lambda_tasa = 0.5 

U = np.random.uniform(0, 1, size=N)

var_exponencial_inversa = -np.log(U) / lambda_tasa

var_exponencial_numpy = np.random.exponential(scale=1/lambda_tasa, size=N)

print("--- Distribución Exponencial (lambda = 0.5) por Transformada Inversa ---")
print(f"Primeros 5 valores generados: {var_exponencial_inversa[:5]}\n")
print(f"Primeros 5 valores (NumPy nativo): {var_exponencial_numpy[:5]}")

plt.figure(figsize=(6, 4))
plt.hist(var_exponencial_inversa, bins=50, density=True, alpha=0.7, color='gold')
plt.title('Exponencial por Transformada Inversa')
plt.xlabel('Valores')
plt.ylabel('Densidad')
plt.grid(axis='y', alpha=0.5)
plt.show()