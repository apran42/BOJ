#include <stdio.h>
int main() {
	int num1 = 0, num2 = 0; int score[1000] = { 0, }; int sum = 0; int hs = 0; double res = 0;
	scanf("%d", &num1);
	for (int i = 0; i < num1; i++)
	{
		scanf("%d", &num2);
		sum = 0;
		for (int j = 0; j < num2; j++)
		{
			scanf("%d", &score[j]);
			sum += score[j];
		}
		hs = 0;
		for (int k = 0; k < num2; k++)
		{
			if (score[k] > sum / num2)
			{
				hs++;
			}
		}
		res = (double)hs / num2;
		printf("%.3lf%%\n", res * 100);
	}
	return 0;
}