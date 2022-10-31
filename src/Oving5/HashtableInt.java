package Oving5;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Objects;

/**
 * Created by Magnus on 19.09.2017.
 *
 * @author Magnus Conrad Hyll (magnus@hyll.no)
 */
public class HashtableInt {
    private static final double A_CONST = (Math.sqrt(5) - 1) / 2;

    private Integer[] values;
    private int collisions;

    public HashtableInt(int length) {
        values = new Integer[length];
        collisions = 0;
    }

    public Integer get(int key) {
        int h1 = hashVal(key);
        if (Objects.equals(values[h1], key)) {
            return values[h1];
        }
        else {
            System.out.println("  Kollisjon med " + values[h1]);
            int h2 = hash2Val(key);
            for (int i = 1; i <= values.length; i++) {
                int index = probe(h1, h2, i);
                if (values[index] == null) {
                    System.out.println("Fant ikke verdien!");
                    return null;
                }
                if (Objects.equals(values[index], key)) {
                    return key;
                }
                System.out.println("  Kollisjon med " + values[index]);
            }
            return null;
        }
    }

    public boolean put(int key) {
        int h1 = hashVal(key);
        if (values[h1] == null) {
            values[h1] = key;
            return true;
        }
        else {
            int h2 = hash2Val(key);
            for (int i = 1; i <= values.length; i++) {
                collisions++;
                int index = probe(h1, h2, i);
                if (values[index] == null) {
                    values[index] = key;
                    return true;
                }
                else {
                }
            }
        }
        System.out.println("Fikk ikke til å sette inn verdien!");
        return false;
    }

    public static void main(String[] args) {
        HashtableInt tall = new HashtableInt(6000011);
        int[] random = new int[5000000];

        for (int i = 0; i < random.length; i++) {
            random[i] = (int) (Math.random() * 1000000000);
        }

        long start = System.nanoTime();
        for (int rand : random) {
            tall.put(rand);
        }
        long delta = System.nanoTime() - start;
        System.out.println("Tid, HashtableInt: " + (delta / 1000000000.0) + " s");
        System.out.println("Antall kollisjoner: " + tall.collisions);

        HashMap<Integer, Integer> tall2 = new HashMap<>();
        start = System.nanoTime();
        for (int rand : random) {
            tall2.put(rand, rand);
        }
        delta = System.nanoTime() - start;
        System.out.println("\nTid, java.util.HashMap: " + (delta / 1000000000.0) + " s");

    }

    private int hashVal(int key) {
        return (int) (values.length * (A_CONST * key - (int) (A_CONST * key)));
    }

    private int hash2Val(int key) {
        return key % (values.length - 1) + 1;
    }

    private int probe(int h1, int h2, int i) {
        return (h1 + i * h2) % values.length;
    }
}
