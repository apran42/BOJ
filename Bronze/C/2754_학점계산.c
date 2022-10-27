#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    char grade[2];
    scanf("%s", grade);
    double res = 0;
    switch (grade[0])
    {
    case 'A': res += 4;
        break;
    case 'B': res += 3;
        break;
    case 'C': res += 2;
        break;
    case 'D': res += 1;
        break;
    default:
        break;
    }
    switch (grade[1])
    {
    case '+': res += 0.3;
        break;
    case '-': res -= 0.3;
        break;
    default:
        break;
    }
    printf("%.1lf", res);
    
    return 0;
}