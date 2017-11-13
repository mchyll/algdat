package Oving12;

public class ByteBuffer {

    private byte[] buffer;
    private int realSize;

    public ByteBuffer(int initSize) {
        if (initSize < 0) {
            throw new IllegalArgumentException("Illegal buffer size: " + initSize);
        }

        buffer = new byte[initSize];
        realSize = 0;
    }

    public void put(int index, byte b) {
        ensureSize(index);
        if (index > realSize) {
            realSize = index;
        }
        buffer[index] = b;
    }

    private void ensureSize(int size) {
        if (buffer.length <= size) {
            byte[] newBuffer = new byte[(int) (1.5 * buffer.length)];
            System.arraycopy(buffer, 0, newBuffer, 0, buffer.length);
            buffer = newBuffer;
        }
    }

    public byte get(int index) {
        if (index >= buffer.length) {
            return 0;
        }

        return buffer[index];
    }

    public byte[] get() {
        byte[] trimmedBuffer = new byte[realSize];
        System.arraycopy(buffer, 0, trimmedBuffer, 0, realSize);
        return trimmedBuffer;
    }
}
