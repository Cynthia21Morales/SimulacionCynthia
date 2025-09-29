set.seed(456)
N <- 200 # Número de valores (simulaciones) a generar en cada caso

media <- 100
desviacion_estandar <- 15
var_normal <- rnorm(N, mean = media, sd = desviacion_estandar)

cat("1. Normal (primeros 5 valores):\n")
print(head(var_normal, 5))

hist(var_normal, 
     main = "Distribución Normal", 
     xlab = "Valores", 
     col = "lightcoral", 
     border = "white")