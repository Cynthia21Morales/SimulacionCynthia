import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

N = 10000        
lambda_tasa = 0.5 

U = np.random.uniform(0, 1, size=N)

var_exponencial_inversa = -np.log(U) / lambda_tasa

print("--- Transformada Inversa para Exponencial ---")
print(f"Primeros 5 valores: {var_exponencial_inversa[:5]}\n")

var_exponencial_numpy = np.random.exponential(scale=1/lambda_tasa, size=N)
print(f"Primeros 5 valores (NumPy nativo): {var_exponencial_numpy[:5]}")

plt.figure(figsize=(6, 4))
plt.hist(var_exponencial_inversa, bins=50, density=True, alpha=0.7, color='gold')
plt.title('Exponencial por Transformada Inversa')
plt.show()