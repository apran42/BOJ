#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int arr[100001] = { 0, };

int main()
{
	int n, count;
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &count);
		arr[count]++;
	}
	for (int i = 0; i < 100001; i++)
	{
		while (arr[i] != 0)
		{
			printf("%d\n", i);
			arr[i]--;
		}
	}
	// system("pause");
	
	return 0;
}