#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
    int n, temp;
    int arr[1001]={0};
    scanf("%d", &n);
    for(int i=0; i<n; i++) {
        scanf("%d", &arr[i]);
    }
    for(int i=0; i<n; i++) {
        for(int j=0; j<n-1; j++) {
            if(arr[j]>arr[j+1])
            {
                temp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=temp;
            }
        }
    }
    for(int i=0; i<n; i++) {
        printf("%d\n", arr[i]);
    }
    return 0;
}