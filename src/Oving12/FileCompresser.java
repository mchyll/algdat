package Oving12;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class FileCompresser {

    public static void compress(String inputFile, String outputFile) {
        try {
            byte[] input = Files.readAllBytes(Paths.get(inputFile));
            byte[] output = LZ.compress(input);
            Files.write(Paths.get(outputFile), output);

            double ratio = (double) output.length / input.length;
            System.out.println("Input: " + input.length + ", output: " + output.length + ", ratio: " + ratio);

        } catch (IOException e) {
            System.err.println("IO error: " + e.getMessage());
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        compress("C:\\Users\\Magnus\\Desktop\\vg3", "C:\\Users\\Magnus\\Desktop\\vg3.lz");
    }
}
