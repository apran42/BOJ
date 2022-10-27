#include <stdio.h>

int main()
{
    int n = 0;
    scanf("%d", &n);
    int fivo[45]={ 0, };
    fivo[0] = 0;
    fivo[1] = 1;
    for (int i = 2; i <= n; i++)
    {
        fivo[i] = fivo[i - 1] + fivo[i - 2];
    }
    
    printf("%d", fivo[n]);
    return 0;
}