import java.util.Random;
public class MetodoDeComposicion {

    private final Random generador = new Random();
    private final double p1, mu1, sigma1, mu2, sigma2;

    public MetodoDeComposicion(double p1, double mu1, double sigma1, double mu2, double sigma2) {
        this.p1 = p1;
        this.mu1 = mu1;
        this.sigma1 = sigma1;
        this.mu2 = mu2;
        this.sigma2 = sigma2;
        generador.setSeed(42); 
    }

    public double generarMuestra() {

        double U = generador.nextDouble();

        if (U < p1) {

            return generador.nextGaussian() * sigma1 + mu1;
        } else {
         
            return generador.nextGaussian() * sigma2 + mu2;
        }
    }

    public static void main(String[] args) {

        double P1 = 0.6;
        double MU1 = 10.0;
        double SIGMA1 = 1.5;
        double MU2 = 20.0;
        double SIGMA2 = 2.0;

        MetodoDeComposicion generadorMezcla = new MetodoDeComposicion(P1, MU1, SIGMA1, MU2, SIGMA2);

        int N = 10000;
        double[] muestras = new double[N];

        for (int i = 0; i < N; i++) {
            muestras[i] = generadorMezcla.generarMuestra();
        }
  
        System.out.println("Primeras 10 muestras generadas:");
        for (int i = 0; i < 10; i++) {
            System.out.printf("%.4f%s", muestras[i], (i < 9 ? ", " : "\n"));
        }
    }
}