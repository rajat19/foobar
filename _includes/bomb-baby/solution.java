class Solution {
	public static long multiplier(long a, long b) {
		long diff = a - b;
		return (diff / b) + 1;
	}

	public static String solution(String x, String y) {
		long step = 0L, m = Long.parseLong(x), f = Long.parseLong(y);
		while (true) {
			if (m <= 0 || f <= 0) break;
			if (m > 100 || f > 100) {
				if (m > f) {
					long mul = Solution.multiplier(m, f);
					m -= f * mul;
					step += mul;
				} else if (f > m) {
					mul = Solution.multiplier(f, m);
					f -= m * mul;
					step += mul;
				} else {
					break;
				}
			} else {
				if (m > f) m-= f;
				else if (f > m) f -= m;
				else break;
				step += 1;
			}
		}

		if (m == 1 && f == 1 && step >= 0) {
			return Long.toString(step);
		}
		return "impossible";
	}

	public static void main(String[] args) {
		String m1 = "2", f1 = "1";
		System.out.println(Solution.solution(m1, f1));

		String m2 = "4", f2 = "7";
		System.out.println(Solution.solution(m2, f2));
	}
}
