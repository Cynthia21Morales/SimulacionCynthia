import numpy as np
import matplotlib.pyplot as plt

np.random.seed(999)

N = 10000        
k = 4            
lambda_tasa = 0.5 
scale = 1 / lambda_tasa 

var_erlang_convolucion = np.zeros(N)

print(f"Generando {N} muestras de Erlang({k}, λ={lambda_tasa}) mediante convolución...")

for i in range(k):
    
    Y_i = np.random.exponential(scale=scale, size=N)
    
    var_erlang_convolucion += Y_i

var_erlang_nativa = np.random.gamma(shape=k, scale=scale, size=N)

print("\n--- Resultados de Muestras Generadas ---")
print(f"Primeros 5 valores (Convolución): {var_erlang_convolucion[:5].round(4)}")
print(f"Primeros 5 valores (NumPy Nativo): {var_erlang_nativa[:5].round(4)}")

plt.figure(figsize=(7, 5))
plt.hist(var_erlang_convolucion, bins=50, density=True, alpha=0.7, color='darkcyan', label='Convolución (Suma de Exponenciales)')
plt.hist(var_erlang_nativa, bins=50, density=True, alpha=0.5, color='red', label='NumPy Nativo (Gamma)')
plt.title(f'Distribución Erlang(k={k}, $\\lambda$={lambda_tasa})')
plt.xlabel('Valores')
plt.ylabel('Densidad')
plt.legend()
plt.grid(axis='y', alpha=0.5)
plt.show()