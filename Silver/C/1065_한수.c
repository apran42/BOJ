#include <stdio.h>

int main()
{
	int n = 0;
	scanf("%d", &n);
	int res = han(n);
	printf("%d", res);
	return 0;
}

int han(int n)
{
	int res = 0;
	for (int i = 1; i <= n; i++)
	{
		if (i < 100)
		{
			res++;
		}
		else
		{
			int a = i / 100;
			int b = i / 10 % 10;
			int c = i % 10;
			if (b - a == c - b)
			{
				res++;
			}
		}
	}

	return res;
}