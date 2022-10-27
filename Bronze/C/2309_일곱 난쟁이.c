#include <stdio.h>
int main()
{
	int height[9] = { 0 };
	int sum = 0;
	for (int i = 0; i < 9; i++)
	{
		scanf("%d", &height[i]);
		sum += height[i];
	}

	int temp  = 0;

	for (int i = 0; i < 9; i++)
	{
		int out = 0;
		for (int j = i + 1; j < 9; j++)
		{
			if (sum - (height[i] + height[j]) == 100)
			{
				height[i] = 0;
				height[j] = 0;
				out = 1;
				break;
			}
		}
		if (out == 1)
		{
			break;
		}
	}

	for (int i = 0; i < 9; i++)
	{
		for (int j = i + 1; j < 9; j++)
		{
			if (height[i] > height[j])
			{
				temp = height[i];
				height[i] = height[j];
				height[j] = temp;
			}
		}
	}

	for (int i = 0; i < 9; i++)
	{
		if (height[i] != 0)
		{
			printf("%d\n", height[i]);
		}
	}

	return 0;

}
