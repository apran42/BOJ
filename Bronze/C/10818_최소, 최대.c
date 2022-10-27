#include <stdio.h>
int main(void) {
    int N = 0, max = 0, min = 0;
    scanf("%d", &N);
    int arr[10000000];
    for (int i = 0; i < N; i++)
    {
        scanf("%d", &arr[i]);
    }
    max = arr[0];
    min = arr[0];
    for (int j = 0; j < N; j++)
    {
        if (max <= arr[j])
        {
            max = arr[j];
        }
    }
    for (int k = 0; k < N; k++)
    {
        if (min >= arr[k])
        {
            min = arr[k];
        }
    }
    printf("%d %d", min, max);
    return 0;
}