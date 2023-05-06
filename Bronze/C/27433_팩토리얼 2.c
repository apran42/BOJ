#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

long long fact(int);

int main() {
	int n;
	scanf("%d", &n);
	printf("%lld", fact(n));
}
long long fact(int n) {
	static long long res = 1;
	
	if (n > 1) {
		res *= n;
		fact(n - 1);
	}
	else
		return res;
}