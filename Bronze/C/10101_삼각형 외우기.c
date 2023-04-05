#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int arr[3];
	for (int i = 0; i < 3; i++)
		scanf("%d", &arr[i]);
	if (arr[0] == 60 && arr[1] == 60 && arr[2] == 60)
		puts("Equilateral");
	else if ((arr[0] + arr[1] + arr[2] == 180) &&
		(arr[0] == arr[1] || arr[0] == arr[2] || arr[1] == arr[2]))
		puts("Isosceles");
	else if ((arr[0] + arr[1] + arr[2] == 180) &&
		(arr[0] != arr[1] && arr[0] != arr[2] && arr[1] != arr[2]))
		puts("Scalene");
	else
		puts("Error");
}