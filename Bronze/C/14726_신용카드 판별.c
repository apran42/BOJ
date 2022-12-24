#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

char isAvailable(char[]);

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		char creditcard[17];
		scanf("%s", creditcard);
		char res = isAvailable(creditcard);
		printf("%c\n", res);
	}
}

char isAvailable(char a[]) {
	for (int i = 0; i < 15; i += 2) {
		int tmp = (int)a[i] - 48;
		if (tmp * 2 < 10)
			a[i] = (char)(tmp * 2 + 48);
		else {
			a[i] = (char)(tmp * 2 / 10 + tmp * 2 % 10 + 48);
		}
	}

	int sum = 0;

	for (int i = 0; i < 16; i++) {
		sum += (int)a[i] - 48;
	}

	if (sum % 10 == 0)
		return 'T';
	else
		return 'F';

}