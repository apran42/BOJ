#include <stdio.h>

int main()
{
    long long n = 0, m = 0;
    scanf("%lld %lld", &n, &m);
    long long res = n - m;
    if (res < 0)
    {
        res *= -1;
    }
    printf("%lld", res);
    
    return 0;
}