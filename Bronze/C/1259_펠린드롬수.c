#include <stdio.h>

int main()
{
  int n;
  while(1)
    {
      scanf("%d", &n);
      if(n==0)
        break;
      else
      {
        if(n>9999)
        {
          if((n/10000==n%10)&&(n/1000%10==n/10%10))
            puts("yes");
          else
            puts("no");
        }
        else if(n>999)
        {
          if((n/1000==n%10)&&(n/100%10==n/10%10))
            puts("yes");
          else
            puts("no");
        }
        else if(n>99)
        {
          if(n/100==n%10)
            puts("yes");
          else
            puts("no");
        }
        else if(n>9)
        {
          if(n/10==n%10)
            puts("yes");
          else
            puts("no");
        }
        else
          puts("yes");
      }
    }
  return 0;
}