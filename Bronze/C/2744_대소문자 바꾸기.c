#include <stdio.h>
#include <string.h>
int main()
{
    char arr[100];
    scanf("%s", arr);
    for(int i=0; i<strlen(arr); i++)
    {
        if((int)arr[i]>96)
            arr[i]-=32;
        else
            arr[i]+=32;
    }
    printf("%s", arr);
    return 0;
}