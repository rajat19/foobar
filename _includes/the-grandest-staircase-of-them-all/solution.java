class Solution {

    public static int solution(int n) {
        int[][] arr = new int[n+1][n+1];
        arr[0][0] = 1;
        for (int i = 1; i < n+1; i++) {
            for (int j = 0; j < n+1; j++) {
                arr[i][j] = arr[i-1][j];
                if (j >= i) {
                    arr[i][j] += arr[i-1][j-i];
                }
            }
        }
        return arr[n][n] - 1;
    }

    public static void main(String[] args) {
        int n1 = 3;
        System.out.println(Solution.solution(n1));

        int n2 = 200;
        System.out.println(Solution.solution(n2));
    }
}
