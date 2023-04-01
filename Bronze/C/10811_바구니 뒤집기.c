#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int main() {
	int n, m, i, j, tmp, a, b;
	int arr[100] = { 0, };
	scanf("%d %d", &n, &m);
	for (a = 0; a < n; a++)
		arr[a] = a + 1;
	for (b = 0; b < m; b++) {
		scanf("%d %d", &i, &j);
		for (a = 0; a < (j - i + 1) / 2; a++) {
			tmp = arr[i - 1 + a];
			arr[i - 1 + a] = arr[j - 1 - a];
			arr[j - 1 - a] = tmp;
		}
	}
	for (b = 0; b < n; b++)
		printf("%d ", arr[b]);
}