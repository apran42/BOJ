#include <stdio.h>

int func(int a, int b);

int main()
{
    int a=0, b=0, pc=1;
    int data=0, cnt=0;
    scanf("%d", &cnt);
    for(int i=0; i<cnt; i++)
    {
        scanf("%d %d", &a, &b);
        pc=func(a, b);
        printf("%d\n", pc);        
    }
    
    return 0;
}

int func(int a, int b)
{
    a%=10;
    int result=0;
    if(a==2)
    {
        switch(b%4)
        {
            case 0:
                result=6; break;
            case 1:
                result=2; break;
            case 2:
                result=4; break;
            case 3:
                result=8; break;
            default:
                break;
        }
    }
    if(a==3)
    {
        switch(b%4)
        {
            case 0:
                result=1; break;
            case 1:
                result=3; break;
            case 2:
                result=9; break;
            case 3:
                result=7; break;
            default:
                break;
        }
    }
    if(a==7)
    {
        switch(b%4)
        {
            case 0:
                result=1; break;
            case 1:
                result=7; break;
            case 2:
                result=9; break;
            case 3:
                result=3; break;
            default:
                break;
        }
    }
    if(a==8)
    {
        switch(b%4)
        {
            case 0:
                result=6; break;
            case 1:
                result=8; break;
            case 2:
                result=4; break;
            case 3:
                result=2; break;
            default:
                break;
        }
    }
    if(a==4)
    {
        if(b%2==0)
            result=6;
        else
            result=4;
    }
    if(a==9)
    {
        if(b%2==0)
            result=1;
        else
            result=9;
    }
    if(a==0)
        result=10;
    if(a==1||a==5||a==6)
        result=a;
    return result;
}