#include <stdio.h>
int main() {
	int num; 
	scanf("%d", &num);
	int res1 = integer1(num); int res2 = integer2(num);
	if (num == 1) printf("1/1");
	else if (res1 % 2 == 0) printf("%d/%d", res1 - (num - res2), num - res2);
	else printf("%d/%d", num - res2, res1 - (num - res2));
	return 0;
}
int integer1(int num) {
	int n = 2;
	while (1)
	{
		if (num == 1) break;
		else if (num > ((n + 1) * (n - 2) / 2 + 1)) n++;
		else break;
	}
	return n;
}
int integer2(int num) {
	int n = 0;
	while (1)
	{
		if (num == 1) break;
		else if (num > ((n + 3) * n / 2 + 1)) n++;
		else break;
	}
	n = n * (n + 1) / 2;
	return n;
}