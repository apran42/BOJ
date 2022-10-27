#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

double fac(double a);

int main()
{
	double n = 0, r = 0, res = 0;
    
    scanf("%lf %lf", &n, &r);
    res = fac(n) / (fac(r) * fac(n - r));
    printf("%.0lf\n", res);

	return 0;
}
double fac(double a)
{
	double res = 1;
	if (a > 0)
		res = a * fac(a - 1);
	return res;
}