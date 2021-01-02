class Braille {
    public static String space = "000000";
    public static String upper = "000001";
    public static String[] alpha = {
        "100000", // a
        "110000", // b
        "100100", // c
        "100110", // d
        "100010", // e
        "110100", // f
        "110110", // g
        "110010", // h
        "010100", // i
        "010110", // j
        "101000", // k
        "111000", // l
        "101100", // m
        "101110", // n
        "101010", // o
        "111100", // p
        "111110", // q
        "111010", // r
        "011100", // s
        "011110", // t
        "101001", // u
        "111001", // v
        "010111", // w
        "101101", // x
        "101111", // y
        "101011", // z
    };

    public static String getValue(char c) {
        if (c == ' ') return space;
        StringBuilder s = new StringBuilder();
        int diff = 0;
        if (c >= 'A' && c <= 'Z') {
            diff = (int) c - (int) 'A';
            s.append(upper);
        } else {
            diff = (int) c - (int) 'a';
        }
        s.append(alpha[diff]);
        return s.toString();
    }
}

class Solution {
    public static String solution(String plaintext) {
        int len = plaintext.length();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < len; i++) {
            char c = plaintext.charAt(i);
            sb.append(Braille.getValue(c));
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        String plaintext1 = "code";
        System.out.println(Solution.solution(plaintext1));

        String plaintext2 = "Braille";
        System.out.println(Solution.solution(plaintext2));
    }
}
