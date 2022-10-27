#include <stdio.h>

int main(void) {
    int a = 0, b = 0;
	for (int i = 1; i > 0; i++)
	{
		scanf("%d %d", &a, &b);
		if (a + b == 0)
		{
			break;
		}
		printf("%d\n", a + b);
	}
	return 0;
}