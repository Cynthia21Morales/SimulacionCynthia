import java.util.Random;

public class MetodosParaGenerarVariablesAleatorias {

    public static void main(String[] args) {
        Random random = new Random(2024);
        int N = 5; 
        int intentos = 0;
        int aceptados = 0;
        
        System.out.println("\n--- Aceptación-Rechazo (Círculo en Cuadrado Unitario) ---\n");

        while (aceptados < N) {
            intentos++;
            
            double x = random.nextDouble();
            double y = random.nextDouble();
            
            
            if (Math.pow(x, 2) + Math.pow(y, 2) <= 1.0) {
               
                aceptados++;
                System.out.printf("Aceptado (%d/%d): (x=%.4f, y=%.4f)\n", aceptados, N, x, y);
            } else {
            }
        }
        
        double eficiencia = (double) N / intentos;
        System.out.printf("\nTotal de Intentos: %d. Eficiencia: %.2f%%\n", intentos, eficiencia * 100);
    }
}