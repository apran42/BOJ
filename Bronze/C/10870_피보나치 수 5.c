#include <stdio.h>
int main()
{
	int n = 0;
	scanf("%d", &n);

	int fibonacci[21] = { 0 };
	fibonacci[0] = 0;
	fibonacci[1] = 1;
	for (int i = 2; i < 21; i++)
	{
		fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2];
	}

	printf("%d", fibonacci[n]);

	return 0;

}
