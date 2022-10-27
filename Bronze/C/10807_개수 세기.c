#include <stdio.h>
int main()
{
    int n=0, tmp=0, chk=0, cnt=0;
    int arr[100];
    scanf("%d", &n);
    for(int i=0; i<n; i++)
    {
        scanf("%d", &tmp);
        arr[i]=tmp;
    }
    scanf("%d", &chk);
    for(int j=0; j<n; j++)
    {
        if(arr[j]==chk)
            cnt++;
    }
    printf("%d", cnt);
    return 0;
}