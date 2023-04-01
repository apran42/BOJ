#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int main() {
	int n, m, i, j, a;
	int arr[100] = { 0, };
	scanf("%d %d", &n, &m);
	for (a = 0; a < n; a++)
		arr[a] = a + 1;
	for (int b = 0; b < m; b++) {
		scanf("%d %d", &i, &j);
		a = arr[i - 1];
		arr[i - 1] = arr[j - 1];
		arr[j - 1] = a;
	}
	for (a = 0; a < n; a++)
		printf("%d ", arr[a]);
}