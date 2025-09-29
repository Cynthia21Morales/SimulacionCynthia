set.seed(42)

N <- 10000        
lambda <- 0.5    


U <- runif(N)

var_exponencial_inversa <- (-1 / lambda) * log(U)

var_exponencial_rexp <- rexp(N, rate = lambda)


cat("--- Transformada Inversa ---\n")
print(head(var_exponencial_inversa, 5))
cat("\n--- Función nativa R (rexp) ---\n")
print(head(var_exponencial_rexp, 5))


hist(var_exponencial_inversa, 
     main = "Exponencial por Transformada Inversa", 
     col = "gold", 
     freq = FALSE)
curve(dexp(x, rate = lambda), add = TRUE, col = "red", lwd = 2)