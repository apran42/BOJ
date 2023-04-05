#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int n, a, b, x[2] = { 0,0 }, y[2] = { 0, };
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d %d", &a, &b);
		if (n < 2) {
			break;
		}
		else {
			if (i == 0) {
				x[0] = a;
				y[0] = b;
			}
			else if (i == 1) {
				if (a >= x[0])
					x[1] = a;
				else {
					x[1] = x[0];
					x[0] = a;
				}
				if (b >= y[0])
					y[1] = b;
				else {
					y[1] = y[0];
					y[0] = b;
				}
			}
			else {
				if (a <= x[0])
					x[0] = a;
				if (a >= x[1])
					x[1] = a;
				if (b <= y[0])
					y[0] = b;
				if (b >= y[1])
					y[1] = b;
			}
		}
	}
	printf("%d", (x[1] - x[0]) * (y[1] - y[0]));
}