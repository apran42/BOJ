#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int gongyak(int*, int*);
int gongbae(int*, int*);

int main() {
	int m, n;
	scanf("%d %d", &m, &n);

	int res1 = gongyak(&m, &n);
	int res2 = gongbae(&m, &n);

	printf("%d\n%d", res1, res2);

	return 0;
}

int gongyak(int* p, int* q) {
	int a = *p;
	int b = *q;
	int res = 0;
	if (a == b)
		return a;
	else if (a > b) {
		for (int i = b; i > 0; i--) {
			if (a % i == 0 && a % i == b % i) {
				res = i;
				break;
			}
		}
	}
	else {
		for (int i = a; i > 0; i--) {
			if (a % i == 0 && a % i == b % i) {
				res = i;
				break;
			}
		}
	}
	if (!res)
		return 1;
	else
		return res;

}

int gongbae(int* p, int* q) {
	int a = *p;
	int a1 = a;
	int b = *q;
	int b1 = b;


	if (a == b)
		return a;
	else {
		while (a != b) {
			if (a > b)
				b += b1;
			else
				a += a1;
		}
	}

	return a;
}