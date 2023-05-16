#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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
    char nums[11] = { '\0', };
    scanf("%s", nums);
    int* arr = (int*)malloc(sizeof(int) * (int)strlen(nums));
    for (int i = 0; i < (int)strlen(nums); i++) {
        arr[i] = (int)nums[i] - 48;
    }
    quickSort(arr, 0, (int)strlen(nums) - 1);
    for (int i = (int)strlen(nums) - 1; i >= 0; i--)
        printf("%d", arr[i]);
}