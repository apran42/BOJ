#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int arr[2000001] = { 0, };

int main()
{
	int n, count;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &count);
		count += 1000000;
		arr[count]++;
	}
	for (int i = 0; i < 2000001; i++)
	{
		while (arr[i] != 0)
		{
			printf("%d\n", i-1000000);
			arr[i]--;
		}
	}

	return 0;
}