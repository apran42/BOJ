#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    int ary[6] = { 0, };
    int temp = 0, sum = 0;

    for(int i = 0; i < 5; i++) {
        scanf("%d", &ary[i]);
    }

    for(int i = 0; i < 5; i++) {
        for(int j = 0; j < 4; j++) {
            if(ary[j] > ary[j + 1]) {
                temp = ary[j];
                ary[j] = ary[j + 1];
                ary[j + 1] = temp;
            }
        }
    }

    for(int i = 0; i < 5; i++) {
        sum += ary[i];
    }

    printf("%d\n%d", sum / 5, ary[2]);

    return 0;
}