#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

void QuickSort(int*, int, int);
void BinarySearch(int*, int, int*);

int main() {
	int n, m;
	scanf("%d", &n);
	int* nums_n = (int*)malloc(sizeof(int) * n);

	for (int i = 0; i < n; i++)
		scanf("%d", (nums_n + i));

	scanf("%d", &m);
	int* nums_m = (int*)malloc(sizeof(int) * m);

	for (int i = 0; i < m; i++)
		scanf("%d", (nums_m + i));

	QuickSort(nums_n, 0, n - 1);

	for (int i = 0; i < m; i++) {
		if (NULL != (nums_m + i))
			BinarySearch(nums_n, n, (nums_m + i));
	}

	for (int i = 0; i < m; i++) {
		if (NULL != (nums_m + i))
			printf("%d\n", *(nums_m + i));
	}

	free(nums_n);
	free(nums_m);
}

void QuickSort(int* arr, int l, int r) {
	int s = l, e = r;
	int pivot = *(arr + ((l + r) / 2));	// 배열의 중간위치의 값
	int tmp;
	do
	{
		while (*(arr + s) < pivot)	// pivot의 왼쪽 값 중 pivot 이상의 값을 가지는 인덱스 or pivot 인덱스(0부터)
			s++;
		while (*(arr + e) > pivot)	// pivot의 오른쪽 값 중 pivot 이하의 값을 가지는 인덱스 or pivot 인덱스(n-1부터)
			e--;
		if (s <= e) {			// s(왼쪽에서 시작한 인덱스)가 e(오른쪽에서 시작한 인덱스)보다 왼쪽에 있을 때(교환 가능)
			tmp = *(arr + s);
			*(arr + s) = *(arr + e);
			*(arr + e) = tmp;
			s++;
			e--;
		}
	} while (s <= e);			// s가 e보다 왼쪽에 있을 때까지

	if (l < e)
		QuickSort(arr, l, e);		// 왼쪽 파티션 반복

	if (s < r)
		QuickSort(arr, s, r);		// 오른쪽 파티션 반복
}

void BinarySearch(int* arr, int len, int* target) {
	int low = 0, high = len - 1, mid;

	while (low <= high) {			// -> 탐색 구간의 길이가 1이하일 때까지
		mid = (low + high) / 2;		// 중간값의 인덱스

		if (*(arr + mid) == *target) {	// 중간값이 마침 찾는 값일때
			*target = 1;
			return;
		}
		else if (*(arr + mid) > *target)// 중간값이 찾는 값보다 클 때
			high = mid - 1;
		else				// 중간값이 찾는 값보다 작을 때
			low = mid + 1;
	}
	*target = 0;				// 찾는 값이 없을 때
	return;
}
