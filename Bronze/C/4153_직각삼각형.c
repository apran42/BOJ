#include <stdio.h>
#include <math.h>
int main() {
    int a, b, c;
    int max, tmp;
    while(1)
    {
        tmp=0;
        scanf("%d %d %d", &a, &b, &c);
        if(a==b&&b==c&&a==0)
            break;
        if(a > b && a > c)
            max=a;
        else if(b > a && b > c)
            max=b;
        else
            max=c;
        if(a==max)
        {
            if(pow(b,2)+pow(c,2)==pow(a,2))
                tmp=1;
        }
        else if(b==max)
        {
            if(pow(a,2)+pow(c,2)==pow(b,2))
                tmp=1;
        }
        else
        {
            if(pow(a,2)+pow(b,2)==pow(c,2))
                tmp=1;
        }
        if(tmp==1)
            puts("right");
        else
            puts("wrong");
    }
    return 0;
}
