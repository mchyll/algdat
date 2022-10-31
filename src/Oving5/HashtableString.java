package Oving5;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URL;
import java.util.ArrayList;
import java.util.Objects;

/**
 * Created by Magnus on 18.09.2017.
 *
 * @author Magnus Conrad Hyll (magnus@hyll.no)
 */
public class HashtableString {

    private static final double A_CONST = (Math.sqrt(5) - 1) / 2;

    private String[] values;
    private int collisions;

    public HashtableString(int length) {
        // Finn nærmeste toerpotens
        length = (int) Math.pow(2, Math.ceil(Math.log(length) / Math.log(2)));
        values = new String[length];
        collisions = 0;
    }

    public String get(String key) {
        System.out.println("Leter etter verdien " + key);
        int convertedString = convertStringIndex(key);
        int h1 = hashVal(convertedString);
        if (Objects.equals(values[h1], key)) {
            return values[h1];
        }
        else {
            System.out.println("  Kollisjon med " + values[h1]);
            int h2 = hash2Val(convertedString);
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

    public boolean put(String key) {
        System.out.println("Setter inn verdien " + key);
        int convertedString = convertStringIndex(key);
        int h1 = hashVal(convertedString);
        if (values[h1] == null) {
            values[h1] = key;
            return true;
        }
        else {
            System.out.println("  Kolliderte med " + values[h1]);
            int h2 = hash2Val(convertedString);
            for (int i = 1; i <= values.length; i++) {
                collisions++;
                int index = probe(h1, h2, i);
                if (values[index] == null) {
                    values[index] = key;
                    return true;
                }
                else {
                    System.out.println("  Kolliderte med " + values[index]);
                }
            }
        }
        System.out.println("Fikk ikke til å sette inn verdien!");
        return false;
    }

    private int convertStringIndex(String index) {
        int result = 0;
        for (int i = 0; i < index.length(); i++) {
            char c = index.charAt(i);
            result = (result + c * (1 << i)) & Integer.MAX_VALUE;
        }
        return result;
    }

    public static void main(String[] args) {
        try {
            URL url = new URL("http://www.aitel.hist.no/fag/_alg/hash/navn");
            BufferedReader in = new BufferedReader(new InputStreamReader(url.openStream()));

            ArrayList<String> lines = new ArrayList<>();
            String line;
            while ((line = in.readLine()) != null) {
                line = line.replaceAll("\t", "").trim();
                lines.add(line);
            }

            HashtableString navn = new HashtableString(lines.size());
            lines.forEach(navn::put);

            int occupied = 0;
            for (String val : navn.values) {
                if (val != null) occupied++;
            }
            System.out.println("\nAntall kollisjoner: " + navn.collisions + ", lastfaktor: " + ((double) occupied / navn.values.length));
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }

    private int hashVal(int key) {
        return (int) (values.length * (A_CONST * key - (int) (A_CONST * key)));
    }

    private int hash2Val(int key) {
        return ((2 * Math.abs(key) + 1) & Integer.MAX_VALUE) % values.length;
    }

    private int probe(int h1, int h2, int i) {
        return (h1 + i * h2) % values.length;
    }
}
