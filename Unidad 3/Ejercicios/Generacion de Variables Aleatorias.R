# 1. Fija una semilla (cualquier número entero)
set.seed(42)

# 2. Genera las variables aleatorias
mi_muestra_reproducible <- rnorm(10, mean = 0, sd = 1)

# Si ejecutas las dos líneas anteriores de nuevo, obtendrás exactamente los mismos 10 números.
print(mi_muestra_reproducible)