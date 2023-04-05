#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int a, b, res[2] = { 0, };
	for (int i = 0; i < 3; i++) {
		scanf("%d %d", &a, &b);
		if (i == 0) {
			res[0] = a;
			res[1] = b;
		}
		else if (i == 1) {
			if (a == res[0])
				res[0] -= a;
			else
				res[0] += a;
			if (b == res[1])
				res[1] -= b;
			else
				res[1] += b;
		}
		else {
			if (res[0] == 0)
				res[0] = a;
			else
				res[0] -= a;
			if (res[1] == 0)
				res[1] = b;
			else
				res[1] -= b;
		}
	}
	printf("%d %d", res[0], res[1]);
}