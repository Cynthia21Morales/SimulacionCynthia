import java.util.Random;
public class VariablesAleatoriaContinuas {


    public static void main(String[] args) {
        
        Random random = new Random(101); 

        double varUniformeEstandar = random.nextDouble();
        System.out.println("1. Uniforme [0.0, 1.0): " + varUniformeEstandar);

        double min = 5.0;
        double max = 15.0;
      
        double varUniformeRango = random.nextDouble() * (max - min) + min;
        System.out.println("2. Uniforme [5.0, 15.0): " + varUniformeRango);

        double varNormalEstandar = random.nextGaussian();
        System.out.println("3. Normal Estándar (μ=0, σ=1): " + varNormalEstandar);
        
        double media = 70.0;
        double desvEstandar = 5.0;
        
        double varNormalPersonalizada = random.nextGaussian() * desvEstandar + media;
        System.out.println("4. Normal (μ=70, σ=5): " + varNormalPersonalizada);
    }
}

