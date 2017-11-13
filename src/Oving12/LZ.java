package Oving12;

import java.util.Arrays;

public class LZ {

    /**
     * Compresses an array of bytes.
     * @param input the array of bytes to compress
     * @return a new array containing the compressed data
     */
    public static byte[] compress(byte[] input) {
        byte[] output = new byte[input.length * 3];
        int inPointer = 0, outPointer = 0;

        int uncompressedMarkerPos = 0;
        byte uncompressed = 0;

        while (inPointer < input.length) {
            int lookbehindIndex = Math.max(inPointer - Short.MAX_VALUE, 0);
            short bestBackreference = 0;
            byte bestMatchLen = 0;
            boolean foundMatch = false;

            while (lookbehindIndex < inPointer) {
                byte matchLen = 0;

                // Loop to find the longest match possible starting from lookbehindIndex
                for (int searchLen = 0; inPointer + searchLen < input.length; searchLen++) {
                    if (input[inPointer + searchLen] == input[lookbehindIndex + searchLen]) {
                        // Increment the number of bytes matched
                        if (++matchLen == Byte.MAX_VALUE) {
                            // Stop when the match length reaches max
                            break;
                        }
                    }
                    else {
                        // No more bytes matching
                        break;
                    }
                }

                // Keep this match only if it's long enough and if it's the best match yet
                if (matchLen > 3 && matchLen > bestMatchLen) {
                    bestBackreference = (short) -(inPointer - lookbehindIndex);
                    bestMatchLen = matchLen;
                    foundMatch = true;
                }

                lookbehindIndex++;
            }

            if (foundMatch) {
                if (uncompressed > 0) {
                    // Write uncompressed-marker
                    output[uncompressedMarkerPos] = uncompressed;
                    outPointer++;

                    // Write uncompressed data
                    for (int i = uncompressed; i > 0; i--) {
                        output[outPointer++] = input[inPointer - i];
                    }
                }

                // Write backreference
                output[outPointer++] = (byte) (bestBackreference >> 8);
                output[outPointer++] = (byte) (bestBackreference & 0xff);
                output[outPointer++] = bestMatchLen;

                // Set new uncompressed-marker pos
                uncompressedMarkerPos = outPointer;
                uncompressed = 0;

                // Move inPointer past compressed data
                inPointer += bestMatchLen;
            }
            else {
                // Another byte is incompressible
                // Increase uncompressed counter and check for overflow
                if (++uncompressed == Byte.MAX_VALUE) {
                    // Write uncompressed-marker
                    output[uncompressedMarkerPos] = uncompressed;
                    outPointer++;

                    // Write uncompressed data
                    for (int i = uncompressed; i > 0; i--) {
                        output[outPointer++] = input[inPointer - i];
                    }

                    // Set new uncompressed-marker pos
                    uncompressedMarkerPos = outPointer;
                    uncompressed = 0;
                }

                // Move inPointer to next byte
                inPointer++;
            }
        }

        // Any leftover incompressible data?
        if (uncompressed > 0) {
            // Write uncompressed-marker
            output[uncompressedMarkerPos] = uncompressed;
            outPointer++;

            // Write uncompressed data
            for (int i = uncompressed; i > 0; i--) {
                output[outPointer++] = input[inPointer - i];
            }
        }

        return Arrays.copyOf(output, outPointer);
    }

    public static byte[] decompress(byte[] input) {
        byte[] output = new byte[input.length * 10];
        int inPointer = 0, outPointer = 0;

        while (inPointer < input.length) {
            // Backreference
            if (input[inPointer] < 0) {
                short backref = (short) -(input[inPointer++] << 8 | input[inPointer++]);
                byte len = input[inPointer++];
                for (int i = 0; i < len; i++) {
                    output[outPointer] = output[outPointer - backref];
                    outPointer++;
                }
            }

            // Uncompressed data
            else {
                int uncompressedLen = input[inPointer++];
                for (int i = 0; i < uncompressedLen; i++) {
                    output[outPointer++] = input[inPointer++];
                }
            }
        }

        return Arrays.copyOf(output, outPointer);
    }

    /**
     * Print a description of compressed data.
     * @param compressed the compressed data to describe.
     */
    public static void interpret(byte[] compressed) {
        int pointer = 0;
        while (pointer < compressed.length) {
            // Backreference
            if (compressed[pointer] < 0) {
                short backref = (short) -(compressed[pointer++] << 8 | compressed[pointer++]);
                byte len = compressed[pointer++];
                System.out.print("[look " + backref + " bytes behind, repeat sequence to length " + len + "] ");
            }

            // Uncompressed data
            else {
                int uncompressedLen = compressed[pointer++];
                System.out.print("[" + uncompressedLen + " bytes uncompressed following] ");
                for (int i = 0; i < uncompressedLen; i++) {
                    System.out.print(compressed[pointer++] + " ");
                }
            }
        }
        System.out.println();
    }

    public static void testCompressArray(byte[] array) {
        byte[] compressed = compress(array);
        for (byte by : compressed) {
            System.out.print(by + " ");
        }
        System.out.println();

        double ratio = (double) compressed.length / array.length;
        System.out.println("Input: " + array.length + ", output: " + compressed.length + ", ratio: " + ratio);

        byte[] decompressed = decompress(compressed);

        System.out.println("Decompressed equals input? " + Arrays.equals(array, decompressed) + "\n");
    }

    public static void main(String[] args) {
        testCompressArray(new byte[]{1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,4,5,6,1,2,3,5,4,4,4,4,4,4,4,4,4,4,4,8,2,5,7});
        testCompressArray(new byte[]{7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,7,7,7,7,7,7,7,7,7});
        testCompressArray(new byte[]{3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6});
    }
}
