import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		for (int i = 0; i < num; i++)
		{
			for (int j = 1; j <num - i; j++)
			{
				System.out.printf(" ");
			}
			for (int k = 0; k < i + 1; k++)
			{
				System.out.printf("*");
			}
			System.out.printf("\n");
		}
	}
}