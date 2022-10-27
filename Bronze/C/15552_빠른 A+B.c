#include <stdio.h>
int main(void) {
	int a = 0, b = 0, t = 0;
	scanf("%d", &t);
	for (int i = 1; i > 0; i++)
	{
		scanf("%d %d", &a, &b);
		printf("%d\n", a + b);
		if (i==t)
		{
			break;
		}
	}
	return 0;
}