#include <stdio.h>

int main()
{
  int m, n;
  int chk = 0;
  int min = -1, sum = 0;
  scanf("%d", &m);
  scanf("%d", &n);
  for(int i = m; i <= n; i++)
  {
      if(i!=1)
      {
          for(int j = 2; j < i; j++)
          {
              if(i%j==0)
              {
                  chk=1;
                  break;
              }
          }
          if(chk != 1)
          {
              if(min == -1)
                  min = i; 
                sum += i;
          }
          chk = 0;
      }
  }
      
  if(min != -1)
    printf("%d\n%d", sum, min);
  else
    puts("-1");
  return 0;
}