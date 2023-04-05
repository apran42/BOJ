#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int arr[3];

	for (int i = 0; i < 3; i++)
		scanf("%d", &arr[i]);
	int max = arr[0];
	int idx = 0;
	if (arr[1] > max) {
		max = arr[1];
		idx = 1;
	}
	if (arr[2] > max) {
		max = arr[2];
		idx = 2;
	}
	if (arr[0] == arr[1] && arr[1] == arr[2])
		printf("%d", arr[0] * 3);
	else if (arr[0] + arr[1] + arr[2] - max <= max) {
		max = arr[0] + arr[1] + arr[2] - max - 1;
		printf("%d", arr[0] + arr[1] + arr[2] - arr[idx] + max);
	}
	else
		printf("%d", arr[0] + arr[1] + arr[2]);
}