#include <stdio.h>

int main()
{
    int num, a;
    int cnt = 0, tmp = 0;
    scanf("%d", &num);
    for(int i = 0; i < num; i++)
    {
        scanf("%d", &a);
        if(a!=1)
        {
            for(int j = 2; j < a; j++)
            {
                if(a%j==0)
                {
                    tmp = 1;
                    break;
                }
            }
            if(tmp != 1)
            cnt++;
        }
        tmp = 0;
    }
    printf("%d", cnt);
    return 0;
}