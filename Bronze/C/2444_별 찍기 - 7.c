#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

void blank(int);
void star(int);

int main() {
	int n;
	scanf("%d", &n);
	int b = n - 1;
	for (int i = 1; i <= n; i++) {
		blank(b);
		star(i);
		puts("");
		b--;
	}
	b = 1;
	for (int i = n - 1; i > 0; i--) {
		blank(b);
		star(i);
		puts("");
		b++;
	}
}

void blank(int n) {
	for (int i = 0; i < n; i++)
		printf(" ");
}

void star(int n) {
	for (int k = 1; k < n * 2; k++) {
		if (!k % 2)
			printf(" ");
		else
			printf("*");
	}
}