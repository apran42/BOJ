import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		for	(int i = 0; i < num; i++) {
			int n1 = sc.nextInt();
			int n2 = sc.nextInt();
			System.out.printf("%d\n", n1+n2);
		}
	}
}