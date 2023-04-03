#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>
#include <string.h>

int main() {
	char n[7];
	int b, sum = 0, exp = 0;
	scanf("%s %d", n, &b);
	for (int i = (int)strlen(n) - 1; i >= 0; i--) {
		if ((int)n[i] >= 48 && (int)n[i] <= 57)
			sum += ((int)n[i] - 48) * (int)pow(b, exp++);
		if((int)n[i] >= 65 && (int)n[i] <= 90)
			sum += ((int)n[i] - 55) * (int)pow(b, exp++);
	}
	printf("%d", sum);
}