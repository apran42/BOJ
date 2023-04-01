#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int main() {
	char string[1001];
	int i;
	scanf("%s", string);
	scanf("%d", &i);
	printf("%c", string[i - 1]);
}