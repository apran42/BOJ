import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int h = sc.nextInt();
		int m = sc.nextInt();
		h *= 60;
		int num = sc.nextInt();
		int temp = h + m + num;
		if (temp >= 1440)
			temp -= 1440;
		System.out.printf("%d %d", temp / 60, temp % 60);
	}
}