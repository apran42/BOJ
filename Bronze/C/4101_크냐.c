#include <stdio.h>

int main()
{
    int a=0, b=0;
    while(1)
    {
        scanf("%d %d", &a, &b);
        if(a==b && a==0)
            return 0;
        else
        {
            if(a>b)
                printf("Yes\n");
            else
                printf("No\n");
        }
    }
}