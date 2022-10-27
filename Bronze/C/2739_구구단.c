#include <stdio.h>
int main(void) {
    int n;
    scanf("%d", &n);
    for (int j=1; j < 10; j++)
    {
        printf("%d * %d = %d\n",n, j, n*j);
    }
    return 0;
}