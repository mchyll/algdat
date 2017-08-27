package semester3.algdat;

/**
 * Created by Magnus on 21.08.2017.
 *
 * @author Magnus Conrad Hyll (magnus@hyll.no)
 */
public class Oving1 {

    public static void finnMaksMinVerdi(int[] aksjeEndring) {
        int aksjeVerdi = 0;
        int[] aksjeVerdier = new int[aksjeEndring.length];

        for (int i = 0; i < aksjeEndring.length; i++) {
            aksjeVerdi += aksjeEndring[i];
            aksjeVerdier[i] = aksjeVerdi;
        }

        int besteFortjeneste = -1;
        int selg = -1, kjop = -1;

        for (int i = 0; i < aksjeVerdier.length; i++) {
            for (int j = i + 1; j < aksjeVerdier.length; j++) {
                if (aksjeVerdier[j] - aksjeVerdier[i] > besteFortjeneste) {
                    besteFortjeneste = aksjeVerdier[j] - aksjeVerdier[i];
                    kjop = i;
                    selg = j;
                }
            }
        }

        System.out.println("Kjøp dag: " + kjop + ", selg dag: " + selg);
    }

    public static int[] genRandomData(int antall) {
        int[] data = new int[antall];
        for (int i = 0; i < antall; i++) {
            data[i] = (int) Math.round(Math.random() * 10 - 5);
        }
        return data;
    }

    public static void main(String[] args) {
        int[] data = new int[] {-1, 3, -9, 2, 2, -1, 2, -1, -5};
        test(10000);
        test(20000);
        test(50000);
        test(100000);
        test(200000);
    }

    public static void test(int antall) {
        System.out.println("Prøver med " + antall + " elementer");
        int[] data = genRandomData(antall);
        long start = System.nanoTime();
        finnMaksMinVerdi(data);
        long stop = System.nanoTime();
        System.out.println("Tid: " + (((double) stop - start) / 1000000) + " ms");
    }

}
