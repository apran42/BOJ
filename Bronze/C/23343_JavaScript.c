#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

void Calc(char[], char[], int*);

int main() {
	char x[6], y[6];
	scanf("%s %s", x, y);

	char *p = &x[0], *q = &y[0];
	int chk = 1, res = 0;

	while (*p != '\0') {
		if (!(*p <= '9' && *p >= '0')) {
			chk *= 3;
			break;
		}
		*p++;
	}

	while (*q != '\0') {
		if (!(*q <= '9' && *q >= '0')) {
			chk *= 5;
			break;
		}
		*q++;
	}

	if (chk % 3 == 0 || chk % 5 == 0)
		puts("NaN");
	else {
		Calc(x, y, &res);
		printf("%d", res);
	}

	return 0;
}

void Calc(char x[], char y[], int* p) {
	int lenx = (int)strlen(x), leny = (int)strlen(y);
	int n = 1, sumx = 0, sumy = 0;
	for (int i = lenx - 1; i > -1; i--) {
		sumx += ((int)x[i] - 48) * n;
		n *= 10;
	}
	n = 1;
	for (int i = leny - 1; i > -1; i--) {
		sumy += ((int)y[i] - 48) * n;
		n *= 10;
	}
	*p = sumx - sumy;
}