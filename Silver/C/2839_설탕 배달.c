#include <stdio.h>

int main() {
	int n;
	scanf("%d", &n);
	int res = sugar(n);
	printf("%d", res);
	return 0;
}
int sugar(int n) {
	int a = 0; int temp = n / 5;
	if (n % 5 == 0) a = n / 5;
	else if (n == 3) a = 1;
    else if (n == 7) a = -1;
	else if (temp != 0 && n % 5 == 1) a = temp + 1;
	else if (temp != 0 && n % 5 == 2) a = temp + 2;
	else if (temp != 0 && n % 5 == 3) a = temp + 1;
	else if (temp != 0 && n % 5 == 4) a = temp + 2;
    else a = -1;
	return a;
}