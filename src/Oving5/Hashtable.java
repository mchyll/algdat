package Oving5;

import java.util.Objects;

/**
 * Created by Magnus on 18.09.2017.
 *
 * @author Magnus Conrad Hyll (magnus@hyll.no)
 */
public class Hashtable {

    private static final double A_CONST = (Math.sqrt(5) - 1) / 2;

    private String[] values;

    public Hashtable(int length) {
        // Finn nærmeste toerpotens
        length = (int) Math.pow(2, Math.ceil(Math.log(length) / Math.log(2)));
        values = new String[length];
    }

    public String get(String key) {
        int convertedString = convertStringIndex(key);
        int h1 = hashVal(convertedString);
        if (Objects.equals(values[h1], key)) {
            return values[h1];
        }
        else {
            int h2 = hash2Val(convertedString);
            for (int i = 0; i < values.length; i++) {
                int index = probe(h1, h2, i);
                if (values[index] == null) {
                    return null;
                }
                if (Objects.equals(values[index], key)) {
                    return key;
                }
            }
            return null;
        }
    }

    public void put(String key) {
        int convertedString = convertStringIndex(key);
        int h1 = hashVal(convertedString);
        if (values[h1] == null) {
            values[h1] = key;
        }
        else {
            int h2 = hash2Val(convertedString);
            for (int i = 0; i < values.length; i++) {
                int index = probe(h1, h2, i);
                if (values[index] == null) {
                    values[index] = key;
                    return;
                }
            }
        }
    }

    private int convertStringIndex(String index) {
        int result = 0;
        for (int i = 0; i < index.length(); i++) {
            char c = index.charAt(i);
            result += c * (1 << i);
        }
        System.out.println(index + " converts to " + result);
        return result;
    }

    public static void main(String[] args) {
        Hashtable t = new Hashtable(8);
        t.put("A");
        t.put("B");
        t.put("C");
        t.put("D");
        t.put("E");
        t.put("F");
        t.put("G");
        t.put("H");
        t.put("I");

        for (String s : t.values) {
            System.out.println(s);
        }
    }

    private int hashVal(int key) {
        return (int) (values.length * (A_CONST * key - (int) (A_CONST * key)));
    }

    private int hash2Val(int key) {
        return (2 * Math.abs(key) + 1) % values.length;
    }

    private int probe(int h1, int h2, int i) {
        return (h1 + i* h2) % values.length;
    }
}
