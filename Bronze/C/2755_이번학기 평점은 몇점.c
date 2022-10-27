#define _CRT_SECURE_NO_WARNINGS
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int main()
{
    int n = 0;
    double s_hak = 0, s_grd = 0, temp = 0, hak = 0;
    char a[101], grd[3];
    scanf("%d", &n);

    for (int i = 0; i < n; i++)
    {
        scanf("%s ", a);
        scanf("%lf ", &hak);
        scanf("%s", grd);
        switch (grd[0])
        {
        case 'A': temp += 4;
            break;
        case 'B': temp += 3;
            break;
        case 'C': temp += 2;
            break;
        case 'D': temp += 1;
            break;
        default:
            break;
        }
        switch (grd[1])
        {
        case '+': temp += 0.3;
            break;
        case '-': temp -= 0.3;
            break;
        default:
            break;
        }
        s_hak += hak;
        s_grd += temp * hak;
        temp = 0;
    }

    printf("%.2lf", round((s_grd / s_hak) * 100) / 100);
    
    //system("pause");
    return 0;
}