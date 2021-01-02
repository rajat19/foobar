class Solution {
    public static int solution(int[] x, int[] y) {
        int ans = 0;
        for (int i = 0; i < x.length; i++) {
            ans ^= x[i];
        }
        for (int i = 0; i < y.length; i++) {
            ans ^= y[i];
        }
        return ans;
    }

    public static void main(String[] args) {
        int[] x1 = {13, 5, 6, 2, 5}, y1 = {5, 2, 5, 13};
        System.out.println(Solution.solution(x1, y1));

        int[] x2 = {14, 27, 1, 4, 2, 50, 3, 1}, y2 = {2, 4, -4, 3, 1, 1, 14, 27, 50};
        System.out.println(Solution.solution(x2, y2));
    }
}