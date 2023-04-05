#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int input[2];
	for(int i = 0; i < 2; i++)
		scanf("%d", &input[i]);
	printf("%d", input[0] * input[1]);
}