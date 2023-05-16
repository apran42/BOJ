#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void quickSort(int arr[], int L, int R) {
    int left = L, right = R;
    int pivot = arr[(L + R) / 2];    
    int temp;
    do
    {
        while (arr[left] < pivot)    
            left++;
        while (arr[right] > pivot)    
            right--;
        if (left <= right)    
        {
            temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
            left++;
            right--;
        }
    } while (left <= right);     

    if (L < right)
        quickSort(arr, L, right);    

    if (left < R)
        quickSort(arr, left, R);    
}

int main() {
    int n, k;
    int arr[1000] = { 0, };
    scanf("%d %d", &n, &k);
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    quickSort(arr, 0, n - 1);
    printf("%d", arr[n - k]);
}