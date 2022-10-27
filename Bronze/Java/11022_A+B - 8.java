import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		for (int i = 1; i <= num; i++) {
			int n1 = sc.nextInt();
			int n2 = sc.nextInt();
			System.out.printf("Case #%d: %d + %d = %d\n", i, n1, n2, n1 + n2);
		}
	}
}
