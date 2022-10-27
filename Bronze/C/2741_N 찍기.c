#include <stdio.h>
int main(void) {
	int n = 0;
	scanf("%d", &n);
	for (int i = 1; i > 0; i++)
	{
		printf("%d\n", i);
		if (i==n)
		{
			break;
		}
	}
	return 0;
}