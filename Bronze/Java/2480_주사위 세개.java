import java.util.Scanner;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n1 = sc.nextInt();
		int n2 = sc.nextInt();
		int n3 = sc.nextInt();
		int max;
		if (n1/n2>0&&n1/n3>0)
			max = n1;
		else if (n2/n1>0&&n2/n3>0)
			max = n2;
		else
			max = n3;
		if (n1==n2&&n2==n3)
			System.out.printf("%d", 10000+n1*1000);
		else if (n1==n2&&n2!=n3)
			System.out.printf("%d", 1000+n1*100);
		else if (n2==n3&&n3!=n1)
			System.out.printf("%d", 1000+n2*100);
		else if (n1==n3&&n2!=n3)
			System.out.printf("%d", 1000+n1*100);
		else
			System.out.printf("%d", max*100);
	}
}