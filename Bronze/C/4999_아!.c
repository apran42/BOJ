#include <stdio.h>
#include <string.h>
int main()
{
    char jae[1001];
    char doc[1001];
    scanf("%s", jae);
    scanf("%s", doc);
    if(strlen(jae)>=strlen(doc))
        puts("go");
    else
        puts("no");
    
    return 0;
}