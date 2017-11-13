package Oving12;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;

public class FileCompressor {

    public static void compress(String inputFile, String outputFile) {
        try {
            byte[] input = Files.readAllBytes(Paths.get(inputFile));
            byte[] output = LZ.compress(input);
            Files.write(Paths.get(outputFile), output);

            double ratio = (double) output.length / input.length;
            System.out.println("Input: " + input.length + ", compressed output: " + output.length + ", ratio: " + ratio);

        } catch (IOException e) {
            System.err.println("IO error: " + e.getMessage());
            e.printStackTrace();
        }
    }

    public static void decompress(String inputFile, String outputFile) {
        try {
            byte[] input = Files.readAllBytes(Paths.get(inputFile));
            byte[] output = LZ.decompress(input);
            Files.write(Paths.get(outputFile), output);

            double ratio = (double) output.length / input.length;
            System.out.println("Compressed input: " + input.length + ", decompressed output: " + output.length + ", ratio: " + ratio);

        } catch (IOException e) {
            System.err.println("IO error: " + e.getMessage());
            e.printStackTrace();
        }
    }

    public static void testCompressFile(String inputFile) {
        try {
            byte[] input = Files.readAllBytes(Paths.get(inputFile));
            byte[] compressed = LZ.compress(input);
            byte[] decompressed = LZ.decompress(compressed);

            double ratio = (double) compressed.length / input.length;
            System.out.println("Input: " + input.length + ", compressed output: " + compressed.length + ", ratio: " + ratio);
            System.out.println("Decompressed equals input? " + Arrays.equals(input, decompressed));

        } catch (IOException e) {
            System.err.println("IO error: " + e.getMessage());
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        compress("C:\\Users\\Magnus\\Desktop\\crt.txt", "C:\\Users\\Magnus\\Desktop\\crt.txt.lz");
        decompress("C:\\Users\\Magnus\\Desktop\\crt.txt.lz", "C:\\Users\\Magnus\\Desktop\\crt_orig.txt");
        testCompressFile("C:\\Users\\Magnus\\Desktop\\crt.txt");
    }
}
