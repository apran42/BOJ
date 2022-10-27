#include <stdio.h>

int main()
{
    int stu[30]={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,
                 16,17,18,19,20,21,22,23,24,25,26,27,28,29,30};
    int s_stu=0, a=0, b=0;
    for(int i=0; i<30; i++)
    {
        scanf("%d", &s_stu);
        for(int j=0; j<30; j++)
        {
            if(s_stu==stu[j])
                stu[j]=0;
        }
    }
    for(int i=0; i<30; i++)
    {
        if(stu[i]!=0 && a == 0)
            a=stu[i];
        if(stu[i]!=0 && a != 0)
            b=stu[i];            
    }
    printf("%d\n%d", a, b);
    
    return 0;
}