#include <stdio.h>

int main() {
    int arr[3];
    int tmp=0;
    scanf("%d %d %d", &arr[0], &arr[1], &arr[2]);
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 2; j++) {
            if(arr[j+1] > arr[j]) {
                tmp=arr[j];
                arr[j]=arr[j+1];
                arr[j+1]=tmp;
            }
        }
    }
    printf("%d", arr[1]);
    return 0;
}