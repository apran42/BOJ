#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

double fac(double a);

int main()
{
	double n = 0, r = 0, res = 0;
	int cnt = 0;
	scanf("%d", &cnt);
	for (int i = 0; i < cnt; i++)
	{
		scanf("%lf %lf", &r, &n);
		res = fac(n) / (fac(r) * fac(n - r));
		printf("%.0lf\n", res);
	}
    
	return 0;
}
double fac(double a)
{
	double res = 1;
	if (a > 0)
		res = a * fac(a - 1);
	return res;
}