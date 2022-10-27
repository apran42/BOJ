#include <stdio.h>
int main() {
    int a, b, c = 0; int arr[10] = { 0 }; int temp;
    scanf("%d", &a); scanf("%d", &b); scanf("%d", &c);
    int mtp = a * b * c;
    while (mtp > 0)
    {
        temp = mtp % 10; mtp /= 10; arr[temp]++;
    }
    for (int i = 0; i < 10; i++)
    {
        printf("%d\n", arr[i]);
    }
    return 0;
}