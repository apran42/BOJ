#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

double fac(double a);

int main()
{
	double a, b;
    scanf("%lf %lf", &a, &b);
    a-=1;
    b-=1;
    double res = fac(a)/(fac(b)*fac(a-b));
    printf("%.0lf", res);
    return 0;
}
double fac(double a)
{
	double res = 1;
	if (a > 0)
		res = a * fac(a - 1);
	return res;
}