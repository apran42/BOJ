import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		for (int i = 1; i > 0; i++)
		{
			int n1 = sc.nextInt();
			int n2 = sc.nextInt();
			if (n1 == n2 && n2 == 0)
			{
				break;
			}
			System.out.printf("%d\n", n1 + n2);
		}
	}
}