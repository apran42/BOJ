#include <stdio.h>
#include <stdlib.h>


int main()
{
	int n;
	int sum = 0, tmp = 0;
	char arr[101];
	scanf("%d", &n);
	scanf("%s", arr);

	for (int i = 0; i < n; i++)
	{
		tmp = (int)(arr[i] - '0');
		sum += tmp;
	}

	printf("%d", sum);

	return 0;

}