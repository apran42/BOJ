#include <stdio.h>
int main()
{
    int eum[8];
    int cnt=0;
    scanf("%d %d %d %d %d %d %d %d", &eum[0], &eum[1], &eum[2],
          &eum[3], &eum[4], &eum[5], &eum[6], &eum[7]);
    for(int i=0; i<7; i++)
    {
        if((eum[i]+1==eum[i+1])||(eum[i]-1==eum[i+1]))
            cnt+=1;
    }
    if(cnt==7&&eum[0]==1)
        puts("ascending");
    else if(cnt==7&&eum[0]==8)
        puts("descending");
    else
        puts("mixed");
    return 0;
}