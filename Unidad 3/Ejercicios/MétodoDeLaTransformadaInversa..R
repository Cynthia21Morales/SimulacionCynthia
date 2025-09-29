set.seed(150)

N <- 10000        
lambda <- 0.8    

U <- runif(N)

var_exponencial_inversa <- (-1 / lambda) * log(U)

var_exponencial_nativa <- rexp(N, rate = lambda)

cat("--- Distribución Exponencial (lambda = 0.8) ---\n")
cat("Primeros 5 valores (Transformada Inversa):\n")
print(head(var_exponencial_inversa, 5))
cat("\nPrimeros 5 valores (Función nativa rexp()):\n")
print(head(var_exponencial_nativa, 5))

hist(var_exponencial_inversa, 
     main = "Distribución Exponencial por Transformada Inversa", 
     xlab = "Valores", 
     freq = FALSE, 
     col = "gold", 
     border = "white")

curve(dexp(x, rate = lambda), add = TRUE, col = "red", lwd = 2)