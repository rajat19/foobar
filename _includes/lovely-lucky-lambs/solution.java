import java.util.ArrayList;
import java.util.List;

class LovelyLuckyLambs {
	public static int stingy(int total_lambs) {
		List<Integer> stingyList = new ArrayList<>();
		stingyList.add(1);
		stingyList.add(1);
		int x = 2, total = 2;
		while (x <= total_lambs) {
			int value = stingyList.get(x-1) + stingyList.get(x-2);
			stingyList.add(value);
			total += stingyList.get(x);
			if (total > total_lambs) break;
			x++;
		}
		return stingyList.size();
	}

	public static int generous(int total_lambs) {
		List<Integer> generouList= new ArrayList<>();
		int x = 0, total = 0;
		while (x <= total_lambs) {
			int current = (int) Math.pow(2, x);
			generouList.add(current);
			total += current;
			if (total > total_lambs) break;
			x++;
		}
		return generouList.size();
	}
	
	public static int solution(int total_lambs) {
		return stingy(total_lambs) - generous(total_lambs);
	}

	public static void main(String[] args) {
		int i1 = 143;
		System.out.println(LovelyLambs.solution(i1));

		int i2 = 10;
		System.out.println(LovelyLambs.solution(i2));
	}
}
