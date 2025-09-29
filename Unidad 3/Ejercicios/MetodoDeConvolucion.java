import java.util.Random;

public class MetodoDeConvolucion {

    private static double generateExponential(Random random, double lambda) {
        double media = 1.0 / lambda; 
        double U = random.nextDouble();
        
        return media * (-Math.log(1.0 - U));
    }

    public static void main(String[] args) {
        
        Random random = new Random(505); // 
        int N = 10000;                  
        int k = 4;                      
        double lambda = 0.5;          
        
        double[] varErlangConvolucion = new double[N];

        System.out.println("--- Método de Convolución (Distribución Erlang) ---");
        System.out.printf("Generando %d muestras de Erlang(k=%d, λ=%.2f)\n\n", N, k, lambda);
        
        for (int i = 0; i < k; i++) {
          
            for (int j = 0; j < N; j++) {
                double Y_i = generateExponential(random, lambda);
              
                varErlangConvolucion[j] += Y_i;
            }
        }

        double mediaTeorica = (double) k / lambda; 
        

        double sumaTotal = 0;
        for (double x : varErlangConvolucion) {
            sumaTotal += x;
        }
        double mediaGenerada = sumaTotal / N;
        
        System.out.println("Primeros 5 valores generados (X = Y1 + ... + Yk):");
        for (int i = 0; i < 5; i++) {
            System.out.printf("  %.4f\n", varErlangConvolucion[i]);
        }
        
        System.out.println("\n--- Resumen Estadístico ---");
        System.out.printf("Media Teórica (k/λ): %.4f\n", mediaTeorica);
        System.out.printf("Media Muestral Generada: %.4f\n", mediaGenerada);
    }
}