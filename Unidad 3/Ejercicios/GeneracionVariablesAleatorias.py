import numpy as np

# --- 1. FIJAR SEMILLA (Para reproducibilidad) ---
# Al usar el mismo número (e.g., 42), obtendrás la misma secuencia de números
np.random.seed(42)
N = 1000 # Número de variables a generar

# ----------------------------------------------------------------------
## Distribuciones Continuas

# 1. Distribución Normal (Gaussiana)
# Parámetros: loc (media), scale (desviación estándar)
media = 50
desviacion_estandar = 10
var_normal = np.random.normal(loc=media, scale=desviacion_estandar, size=N)
print(f"Normal (primeros 5): {var_normal[:5]}")

# 2. Distribución Uniforme
# Parámetros: low (límite inferior), high (límite superior)
limite_min = 10
limite_max = 20
var_uniforme = np.random.uniform(low=limite_min, high=limite_max, size=N)
print(f"Uniforme (primeros 5): {var_uniforme[:5]}")

# 3. Distribución Exponencial
# Parámetros: scale (1 / tasa lambda)
tasa_lambda = 0.5
var_exponencial = np.random.exponential(scale=1/tasa_lambda, size=N)
print(f"Exponencial (primeros 5): {var_exponencial[:5]}")

# ----------------------------------------------------------------------
## Distribuciones Discretas

# 4. Distribución Binomial
# Parámetros: n (número de ensayos), p (probabilidad de éxito)
num_ensayos = 10
prob_exito = 0.3
var_binomial = np.random.binomial(n=num_ensayos, p=prob_exito, size=N)
print(f"Binomial (primeros 5): {var_binomial[:5]}")

# 5. Distribución de Poisson
# Parámetros: lam (tasa lambda, promedio de eventos)
tasa_promedio = 4
var_poisson = np.random.poisson(lam=tasa_promedio, size=N)
print(f"Poisson (primeros 5): {var_poisson[:5]}")