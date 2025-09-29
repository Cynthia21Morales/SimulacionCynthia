# Fija la semilla para que los resultados sean siempre los mismos
set.seed(123)
N <- 100 # Número de valores a generar en cada caso

# ----------------------------------------------------------------------
# 1. Distribución Binomial (rbinom)
# Simula el número de 'éxitos' en una serie de ensayos.
# Parámetros: N (número de valores a generar), size (número de ensayos), prob (probabilidad de éxito)
num_ensayos <- 20
prob_exito <- 0.4
var_binomial <- rbinom(N, size = num_ensayos, prob = prob_exito)

cat("1. Binomial (primeros 10 valores):\n")
print(head(var_binomial, 10))
# Opcional: Graficar la distribución
hist(var_binomial, main = "Distribución Binomial", col = "skyblue", breaks = seq(-0.5, max(var_binomial) + 0.5, by = 1))