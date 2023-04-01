#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int main() {
	int n, m, i, j, k;
	int arr[100] = { 0, };
	scanf("%d %d", &n, &m);
	for (int a = 0; a < m; a++)
	{
		scanf("%d %d %d", &i, &j, &k);
		for (int b = i - 1; b < j; b++)
			arr[b] = k;
	}
	for (int i = 0; i < n; i++)
		printf("%d ", arr[i]);
}