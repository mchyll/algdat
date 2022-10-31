/**
 * Created by Magnus on 29.08.2017.
 *
 * @author Magnus Conrad Hyll <magnus@hyll.no>
 */
public class Oving3 {
    public static void bytt(int[] t, int i, int j) {
        int k = t[j];
        t[j] = t[i];
        t[i] = k;
    }

    public static void quicksort(int[] t, int v, int h) {
        if (h - v > 2) {
            int delepos = splitt(t, v, h);
            quicksort(t, v, delepos - 1);
            quicksort(t, delepos + 1, h);
        }
        else {
            median3sort(t, v, h);
        }
    }

    public static int median3sort(int[] t, int v, int h) {
        int m = (v + h) / 2;
        if (t[v] > t[m]) bytt(t, v, m);
        if (t[m] > t[h]) {
            bytt(t, m, h);
            if (t[v] > t[m]) bytt(t, v, m);
        }
        return m;
    }

    public static int splitt(int[] t, int v, int h) {
        int iv, ih;
        int m = median3sort(t, v, h);
        int dv = t[m];
        bytt(t, m, h - 1);
        for (iv = v, ih = h - 1;;) {
            while (t[++iv] < dv);
            while (t[--ih] > dv);
            if (iv >= ih) break;
            bytt(t, iv, ih);
        }
        bytt(t, iv, h - 1);
        return iv;
    }

    public static boolean isSorted(int[] arr) {
        int prev = arr[0];
        for (int i = 1; i < arr.length; i++) {
            if (prev > arr[i]) return false;
            prev = arr[i];
        }
        return true;
    }

    public static void main(String[] args) {
        int len = 100000;
        int[] arr = new int[len];
        System.out.println("Før sort: ");
        for (int i = 0; i < len; i++) {
            arr[i] = len - i;
            System.out.print(arr[i] + " ");
        }
        quicksort(arr, 0, arr.length - 1);

        System.out.println("\nEtter sort: ");
        for (int elem : arr) {
            System.out.print(elem + " ");
        }
        System.out.println("\nEr sortert: " + isSorted(arr));

        System.out.println("\n\nFør sort: ");
        for (int i = 0; i < len; i++) {
            arr[i] = (int) (Math.random() * 150 - 30);
            System.out.print(arr[i] + " ");
        }
        quicksort(arr, 0, arr.length - 1);

        System.out.println("\nEtter sort: ");
        for (int elem : arr) {
            System.out.print(elem + " ");
        }
        System.out.println("\nEr sortert: " + isSorted(arr));
    }
}
