package semester3.algdat;

/**
 * Created by Magnus on 24.08.2017.
 *
 * @author Magnus Conrad Hyll (magnus@hyll.no)
 */
public class Oving2 {
    public static double pow(double x, int n) {
        if (n <= 1) {
            return 1;
        }
        return x * pow(x, n - 1);
    }

    public static void main(String[] args) {
        System.out.println(pow(5, 8));
    }
}
