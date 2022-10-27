#include <stdio.h>
#include <math.h>
int main() {
	double a, b, c;
	scanf("%lf %lf %lf", &a, &b, &c);
	if (b >= c) printf("-1");
	else printf("%.0lf", floor(a / (c - b)) + 1);
	return 0;
}