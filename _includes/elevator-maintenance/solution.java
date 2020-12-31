import java.util.Arrays;

class Elevator implements Comparable<Elevator>{
	int major;
	int minor;
	int revision;
	String str;

	public Elevator(String elevator) {
		String[] div = elevator.split(".");
		this.str = elevator;
		major = Integer.parseInt(div[0]);
		minor = div.length > 1 ? Integer.parseInt(div[1]) : -1;
		revision = div.length > 2 ? Integer.parseInt(div[2]) : -1;
	}

	@Override
	public int compareTo(Elevator o) {
		if (this.major < o.major) return -1;
		if (this.major > o.major) return 1;
		if (this.minor < o.minor) return -1;
		if (this.minor > o.minor) return 1;
		if (this.revision < o.revision) return -1;
		if (this.revision > o.revision) return 1;
		return 0;
	}
}

class ElevatorMaintenance {
	public static String[] solution(String [] elevators) {
		int len = elevators.length;
		Elevator[] els = new Elevator[len];
		for (int i = 0; i < len; i++) {
			els[i] = new Elevator(elevators[i]);
		}
		Arrays.sort(els);
		String [] finals = new String[len];
		for (int j = 0; j < len; j++) {
			finals[i] = els[i].str;
		}
		return finals;
	}

	public static void main(String[] args) {
		String[] l1 = {"1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"};
		System.out.println(ElevatorMaintenance.solution(l1));

		String[] l2 = {"1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"};
		System.out.println(ElevatorMaintenance.solution(l2));
	}
}
