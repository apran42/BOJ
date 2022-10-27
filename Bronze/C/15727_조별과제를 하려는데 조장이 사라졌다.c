#include <stdio.h>

int main()
{
    int l, t;
    scanf("%d", &l);
    t=l/5;
    if(l%5!=0)
        t++;
    printf("%d", t);
    return 0;
}