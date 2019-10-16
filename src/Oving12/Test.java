package Oving12;

public class Test {

    public static String leftPad(String originalString, int length,
                                 char padCharacter) {
        String paddedString = originalString;
        while (paddedString.length() < length) {
            paddedString = padCharacter + paddedString;
        }
        return paddedString;
    }

    public static String shortBits(short s) {
        return leftPad(Integer.toBinaryString(s & 0xffff), 16, '0');
    }

    public static String byteBits(byte s) {
        return leftPad(Integer.toBinaryString(s & 0xff), 8, '0');
    }

    public static void main(String[] args) {
        short test = -321;
        byte b1 = (byte) (test >> 8);
        byte b2 = (byte) (test & 0xff);
        System.out.println("b1=" + b1 + ",   bits=" + byteBits(b1));
        System.out.println("b2=" + b2 + ",  bits=" + byteBits(b2));

        short d1 = (short) (b1 << 8);
        short d2 = (short) (b2 & 0xff);
        System.out.println("d1=" + d1 + ", bits=" + shortBits(d1));
        System.out.println("d2=" + d2 + ",  bits=" + shortBits(d2));

        short d = (short) (d1 | d2);
        System.out.println("test=" + test + ", bits=" + shortBits(test));
        System.out.println("d=" + d + ",    bits=" + shortBits(d));
    }
}
