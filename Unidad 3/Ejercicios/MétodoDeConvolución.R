set.seed(789)

N <- 10000        
k <- 5           
lambda <- 0.2    

var_erlang_convolucion <- rep(0, N)

for (i in 1:k) {
  
  Y_i <- rexp(N, rate = lambda)
  
  var_erlang_convolucion <- var_erlang_convolucion + Y_i
}

var_erlang_nativa <- rgamma(N, shape = k, rate = lambda)

cat("--- Distribución Erlang (k=5, lambda=0.2) por Convolución ---\n")
cat("Primeros 5 valores (Convolución):\n")
print(head(var_erlang_convolucion, 5))
cat("\nPrimeros 5 valores (Función nativa rgamma()):\n")
print(head(var_erlang_nativa, 5))

hist(var_erlang_convolucion, 
     main = paste0("Distribución Erlang (k=", k, ") por Convolución"), 
     xlab = "Valores (Tiempo de Espera)", 
     freq = FALSE, 
     col = "darkcyan", 
     border = "white",
     xlim = range(c(var_erlang_convolucion, var_erlang_nativa)))

lines(density(var_erlang_nativa), col = "red", lwd = 2)
legend("topright", legend = c("Convolución", "Densidad Nativa (rgamma)"), col = c("darkcyan", "red"), lwd = c(NA, 2), fill = c("darkcyan", NA), border = c("white", NA))