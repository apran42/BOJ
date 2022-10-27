#include <stdio.h>
int main()
{
	int a;
	scanf("%d", &a);

	double score[1000] = { 0 };

	for (int i = 0; i < a; i++)
	{
		scanf("%lf", &score[i]);
	}

	double max = score[0];

	for (int i = 0; i < a; i++)
	{
		if (score[i] >= max)
		{
			max = score[i];
		}
	}

	double b = 0;

	for (int i = 0; i < a; i++)
	{
		score[i] = score[i] / max * 100;
		b += score[i];
	}

	printf("%lf", b / a);
}
