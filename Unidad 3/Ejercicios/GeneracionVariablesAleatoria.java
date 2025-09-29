import java.util.Random;
public class GeneracionVariablesAleatoria {

    public static void main(String[] args) {
        Random random = new Random(42); 

        int entero_basico = random.nextInt();
        System.out.println("1. Entero básico: " + entero_basico);

        int entero_hasta_99 = random.nextInt(100);
        System.out.println("2. Entero [0, 99]: " + entero_hasta_99);

        int min = 10;
        int max = 20;
        int entero_en_rango = random.nextInt(max - min + 1) + min;
        System.out.println("3. Entero [10, 20]: " + entero_en_rango);

        double flotante_basico = random.nextDouble();
        System.out.println("4. Flotante [0.0, 1.0): " + flotante_basico);

        double f_min = 5.0;
        double f_max = 15.0;
        double flotante_en_rango = random.nextDouble() * (f_max - f_min) + f_min;
        System.out.println("5. Flotante [5.0, 15.0): " + flotante_en_rango);

    
        boolean booleano_aleatorio = random.nextBoolean();
        System.out.println("6. Booleano: " + booleano_aleatorio);
    }
}

