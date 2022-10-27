#include <stdio.h>
int main(void) {
	int arr[9]; int a = 0;
	for (int i = 0; i < 9; i++)
	{
		scanf("%d", &arr[i]);
	}
	int max = arr[0]; int b = 1;
	for (int j = 0; j < 9; j++)
	{
		if (max <= arr[j])
		{
			max = arr[j];
			b = j + 1;
		}
	}
	printf("%d\n", max);
	printf("%d", b);
	return 0;
}