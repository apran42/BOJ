#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int a, b, n, tmp;
	scanf("%d %d %d", &a, &b, &n);
	tmp = a / b;
	for (int i = 0; i < n; i++) {
		a %= b;
		a *= 10;
		tmp = a / b;
  	}
 	 printf("%d", tmp);
}
