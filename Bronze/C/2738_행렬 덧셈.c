#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int array1[100][100];
int array2[100][100];

int main()
{
	int a = 0, b = 0;
	scanf("%d %d", &a, &b);

	for (int i = 0; i < a; i++)
	{
		for (int j = 0; j < b; j++)
		{
			scanf("%d", &array1[i][j]);
		}
	}

	for (int i = 0; i < a; i++)
	{
		for (int j = 0; j < b; j++)
		{
			scanf("%d", &array2[i][j]);
			array1[i][j] += array2[i][j];
		}
	}

	for (int i = 0; i < a; i++)
	{
		for (int j = 0; j < b; j++)
		{
			if (j == b-1)
				printf("%d", array1[i][j]);
			else
				printf("%d ", array1[i][j]);
		}
		puts("");
	}


	//system("pause");
	return 0;
}