class Solution {
    public static String solution(String s) {
        int l = s.length();
        char[] chars = s.toCharArray();
        for (int i = 0; i < l; i++) {
            char c = chars[i];
            if (c >= 'a' && c <= 'z') {
                int pos = c - 'a';
                chars[i] = (char) ('a' + 25 - pos);
            }
        }
        return String.valueOf(chars);
    }
    
    public static void main(String[] args) {
        String s1 = "wrw blf hvv ozhg mrtsg'h vkrhlwv?";
        System.out.println(Solution.solution(s1));

        String s2 = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!";
        System.out.println(Solution.solution(s2));
    }
}