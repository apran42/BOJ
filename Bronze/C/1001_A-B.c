#include <stdio.h>
int main(void) {
    long double A, B;
    scanf("%Lf", &A);
    scanf("%Lf", &B);
    printf("%.9Lf", A/B);
    return 0;
}