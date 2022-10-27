#include <stdio.h>
int main()
{

	int sum;
	scanf("%d", &sum);
	
	int a;
	scanf("%d", &a);

	int tmp1, tmp2 = 0;

	for (int i = 0; i < a; i++)
	{
		int a, b = 0;
		scanf("%d %d", &a, &b);
		tmp1 = a * b;
		tmp2 += tmp1;
	}

	if (sum == tmp2)
	{
		printf("Yes");
	}
		
	else
	{
		printf("No");
	}

	return 0;

}