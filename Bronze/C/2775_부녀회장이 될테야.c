#include <stdio.h>
int main()
{
	int t; int k; int n;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		scanf("%d", &k);
		scanf("%d", &n);
		int arr1[14] = { 1,2,3,4,5,6,7,8,9,10,11,12,13,14 };
		int arr2[14] = { 1, };
		for (int j = 0; j < k; j++)
		{
			for (int l = 1; l < 14; l++)
			{
				arr2[l] = arr2[l - 1] + arr1[l];
			}
			for (int m = 1; m < 14; m++)
			{
				arr1[m] = arr2[m];
			}
		}
		printf("%d\n", arr2[n - 1]);
	}
	return 0;
}