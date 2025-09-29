generar_composicion <- function(n, p1, lambda1, lambda2) {
  
  X <- numeric(n)
  
  set.seed(123) 

  U <- runif(n)

  for (i in 1:n) {
    if (U[i] < p1) {
      X[i] <- rexp(1, rate = lambda1)
    } else {
      X[i] <- rexp(1, rate = lambda2)
    }
  }
  
  return(X)
}

N <- 10000          
P1 <- 0.5           
P2 <- 1 - P1        
LAMBDA1 <- 0.5      
LAMBDA2 <- 2        

muestras_comp <- generar_composicion(N, P1, LAMBDA1, LAMBDA2)

print("Primeras 10 muestras generadas:")
print(head(muestras_comp, 10))

hist(
  muestras_comp,
  breaks = 50,
  freq = FALSE,
  main = "Histograma de Muestras (Método de Composición)",
  xlab = "Valores generados",
  col = "lightblue",
  border = "black"
)

x_vals <- seq(min(muestras_comp), max(muestras_comp), length.out = 500)
densidad_teorica <- P1 * dexp(x_vals, rate = LAMBDA1) + P2 * dexp(x_vals, rate = LAMBDA2)
lines(x_vals, densidad_teorica, col = "red", lwd = 2)

legend(
  "topright", 
  legend = c("Muestras Generadas", "Densidad Teórica"), 
  col = c("lightblue", "red"), 
  lty = c(NA, 1), 
  lwd = c(NA, 2), 
  pch = c(15, NA), 
  cex = 0.8
)