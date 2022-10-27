#include <stdio.h>
int main(void) {
	int N = 0;
	scanf("%d", &N); 
	for (int i = 0; i < N; i++)
	{
		for (int a = 1; a < N - i; a++)
		{
			printf(" ");
		}
		for (int b = 0; b < i+1; b++)
		{
			printf("*");
		}
		printf("\n");
	}
	return 0;
}