#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	int x1, y1, c, x2, y2, f, X, Y;
	int* num[6] = { &x1, &y1, &c, &x2, &y2, &f };
	for (int i = 0; i < 6; i++) {
		scanf("%d", num[i]);
	}
	if (x1 == 0) {
		int res_y = c / y1;
		int res_x = (f - (res_y * y2)) / x2;
		printf("%d %d", res_x, res_y);
	}
	else if (y1 == 0) {
		int res_x = c / x1;
		int res_y = (f - (res_x * x2)) / y2;
		printf("%d %d", res_x, res_y);
	}
	else if (x2 == 0) {
		int res_y = f / y2;
		int res_x = (c - (res_y * y1)) / x1;
		printf("%d %d", res_x, res_y);
	}
	else if (y2 == 0) {
		int res_x = f / x2;
		int res_y = (c - (res_x * x1)) / y1;
		printf("%d %d", res_x, res_y);
	}
	else {
		if (x1 % x2 == 0 || x2 % x1 == 0) {
			// 위 x1이 클 때
			if (x1 > x2) {
				int tmp = x1 / x2;
				x2 *= tmp;
				y2 *= tmp;
				f *= tmp;
			}
			if (x1 < x2) {
				int tmp = x2 / x1;
				x1 *= tmp;
				y1 *= tmp;
				c *= tmp;
			}
			int tmp_y = y1 - y2;
			int res_y = c - f;
			res_y /= tmp_y; // res_y: y의 값
			c -= (res_y * y1);
			int res_x = c / x1;
			printf("%d %d", res_x, res_y);
		}
		// y1 또는 y2가 서로의 배수일 때
		else if (y1 % y2 == 0 || y2 % y1 == 0) {
			// 위 y1이 클 때
			if (y1 > y2) {
				int tmp = y1 / y2;
				x2 *= tmp;
				y2 *= tmp;
				f *= tmp;
			}
			if (y1 < y2) {
				int tmp = y2 / y1;
				x1 *= tmp;
				y1 *= tmp;
				c *= tmp;
			}
			int tmp_x = x1 - x2;
			int res_x = c - f;
			res_x /= tmp_x; // res_y: y의 값
			c -= (res_x * x1);
			int res_y = c / y1;
			printf("%d %d", res_x, res_y);
		}
		// x1, x2 혹은 y1, y2 어느 것도 서로 배수가 아님
		else {
			int tmp_x1 = x1, tmp_x2 = x2;
			x1 *= tmp_x2;
			y1 *= tmp_x2;
			c *= tmp_x2;
			x2 *= tmp_x1;
			y2 *= tmp_x1;
			f *= tmp_x1;
			int tmp_y = y1 - y2;
			int res_y = c - f;
			res_y /= tmp_y;
			c -= (res_y * y1);
			int res_x = c / x1;
			printf("%d %d", res_x, res_y);
		}
	}
}