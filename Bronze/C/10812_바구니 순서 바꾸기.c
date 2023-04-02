#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int n, m, a, b, c, idx;
	scanf("%d %d", &n, &m);
	int arr[100] = { 0, };
	int arr2[100] = { 0, };

	for (int i = 0; i < n; i++)
		arr[i] = i + 1;

	for (int i = 0; i < m; i++) {
		scanf("%d %d %d", &a, &b, &c);
		idx = 0;
		for (int j = 0; j < c - a; j++)
			arr2[idx++] = arr[a - 1 + j];
		int idx_a = idx;
		idx = -1;
		for (int j = c; j <= b; j++)
			arr[a + idx++] = arr[j-1];
		idx = 0;
		for (int j = a + b - c; j < b; j++)
			arr[j] = arr2[idx++];
		
	}

	for (int i = 0; i < n; i++)
		printf("%d ", arr[i]);
}