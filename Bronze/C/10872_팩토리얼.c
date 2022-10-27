#include <stdio.h>

int main()
{
	int n = 0;
	scanf("%d", &n);
	int res = factorial(n);
	printf("%d", res);
    
    return 0;
}

int factorial(int a)
{
	int res = 1;
	if (a > 0)
		res = a * factorial(a - 1);
	return res;
}