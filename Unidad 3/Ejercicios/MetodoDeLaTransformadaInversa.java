import java.util.Random;
import java.util.stream.DoubleStream;
public class MetodoDeLaTransformadaInversa {
    

    public static void main(String[] args) {
        
        Random random = new Random(305); 
        int N = 5;          
        double lambda = 0.5; 
        
        System.out.println("--- Método de la Transformada Inversa (Distribución Exponencial) ---\n");
        System.out.printf("Parámetros: lambda (tasa) = %.2f\n\n", lambda);
        
        for (int i = 0; i < N; i++) {
            
            double U = random.nextDouble();

            double varExponencial = (-1.0 / lambda) * Math.log(1.0 - U);
            
            System.out.printf("Muestra %d: U = %.6f  ->  X = %.6f\n", 
                              i + 1, U, varExponencial);
        }
        
        System.out.println("\n--- Resumen de 10,000 Valores Generados ---");
        
        DoubleStream streamExponencial = random.doubles(10000)
            .map(U -> (-1.0 / lambda) * Math.log(1.0 - U));
        
        double mediaGenerada = streamExponencial.average().getAsDouble();
        
        double mediaTeorica = 1.0 / lambda; 
        
        System.out.printf("Media Teórica (1/lambda): %.4f\n", mediaTeorica);
        System.out.printf("Media Muestral Generada:  %.4f\n", mediaGenerada);
    }
}

