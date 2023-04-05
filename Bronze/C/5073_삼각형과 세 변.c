#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int arr[3];
	while (1) {
		for (int i = 0; i < 3; i++)
			scanf("%d", &arr[i]);
		int max = arr[0];
		if (arr[1] > max)
			max = arr[1];
		if (arr[2] > max)
			max = arr[2];
		if (arr[0] == 0 && arr[1] == 0 && arr[2] == 0)
			break;
		else {
			if (arr[0] + arr[1] + arr[2] - max > max) {
			if (arr[0] == arr[1] && arr[1] == arr[2] && arr[2] == arr[0])
				puts("Equilateral");
			else if (arr[0] == arr[1] || arr[0] == arr[2] || arr[1] == arr[2])
				puts("Isosceles");
			else
				puts("Scalene");
			}
			else
				puts("Invalid");
		}
	}
}