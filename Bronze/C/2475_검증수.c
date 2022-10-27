#include <stdio.h>
int main() {
    int arr[5]; int sum=0;
    for(int i=0;i<5;i++)
    {
        scanf("%d", &arr[i]);
        sum+=arr[i]*arr[i];
    }
    printf("%d",sum%10);
}