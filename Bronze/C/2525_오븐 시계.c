#include <stdio.h>

int main(void) {
    int a=0, b=0, c=0;
    scanf("%d %d₩n", &a, &b);
    scanf("%d", &c);
    a *= 60;
    int d = a+b+c;
    int e = d/60;
    if (e>=24) {
        e -=24;
    }
    printf("%d %d", e, d%60);
    return 0;

}