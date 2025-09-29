 import java.util.Random;
public class VariablesAleatorias {

    public static void main(String[] args) {
        
        Random random = new Random(101); 
        int numLanzamientos = 10;
        int minValor = 1; 
        int maxValor = 6; 

        System.out.println("Simulación de " + numLanzamientos + " Lanzamientos de Dado:");
        
        
        for (int i = 0; i < numLanzamientos; i++) {
            
            int resultado = random.nextInt(maxValor - minValor + 1) + minValor;
            System.out.println("Lanzamiento " + (i + 1) + ": " + resultado);
        }
        
        System.out.println("\nLanzamiento de moneda (0 = Cruz, 1 = Cara): " + random.nextInt(2));
    }
}
