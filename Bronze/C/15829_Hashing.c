#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int n = 0;
	long long int sum = 0, r = 1;
	char arr[50] = { ' ' };
	long long int mod[50] = { 0, };
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf(" %c", &arr[i]);
	}
	for (int i = 0; i < n; i++) {
		r %= 1234567891;
		mod[i] = (((long long int)arr[i] - 96) * r) % 1234567891;
		r *= 31;
	}
	for (int i = 0; i < n; i++) {
		sum += mod[i];
		if (sum >= 1234567891)
			sum %= 1234567891;
	}
	printf("%lld", sum);
	return 0;
}