#include <stdio.h>
int main() {

	int n = 0; int num = 1;
	scanf("%d", &n);
	if (n == 1)
	{
		printf("%d", num);
	}
	else
	{
		while (1)
		{
			if (n > 3 * num * (num - 1) + 1 && n <= 3 * num * (num + 1) + 1)
			{
				printf("%d", num + 1);
				break;
			}
			else
			{
				num++;
			}
		}
	}
	
	return 0;
}