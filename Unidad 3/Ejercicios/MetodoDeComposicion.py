import numpy as np
import matplotlib.pyplot as plt

def generar_composicion(n, p1, lambda1, lambda2):
   
    np.random.seed(42) 
    
    U = np.random.rand(n)
    
    X = np.empty(n)
    
    idx_comp1 = U < p1
    idx_comp2 = U >= p1
    
    n1 = np.sum(idx_comp1) 
    X[idx_comp1] = np.random.exponential(scale=1/lambda1, size=n1)
    
    n2 = np.sum(idx_comp2) 
    X[idx_comp2] = np.random.exponential(scale=1/lambda2, size=n2)
    
    return X

N = 10000          
P1 = 0.5          
LAMBDA1 = 0.5      
LAMBDA2 = 2        

muestras_comp = generar_composicion(N, P1, LAMBDA1, LAMBDA2)

print(f"Primeras 10 muestras generadas:\n{muestras_comp[:10]}\n")

plt.figure(figsize=(10, 6))

plt.hist(muestras_comp, bins=50, density=True, color='skyblue', edgecolor='black', alpha=0.7, label='Muestras Generadas')

x_vals = np.linspace(0, np.max(muestras_comp), 500)

densidad_teorica = P1 * (LAMBDA1 * np.exp(-LAMBDA1 * x_vals)) + \
                   (1 - P1) * (LAMBDA2 * np.exp(-LAMBDA2 * x_vals))

plt.plot(x_vals, densidad_teorica, color='red', linewidth=2, label='Densidad Teórica')

plt.title('Método de Composición: Mezcla de dos Exponenciales')
plt.xlabel('Valores de la Variable Aleatoria')
plt.ylabel('Densidad de Probabilidad')
plt.legend()
plt.grid(axis='y', alpha=0.5)
plt.show()