#include <stdio.h>
int main() {
	int n = 0, sum = 0, score = 0; char ox[80];
	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		sum = 0;
		score = 1;
		scanf("%s", ox);
		for (int j = 0; j < strlen(ox); j++)
		{
			if (ox[j] == 'O')
			{
				sum += score;
				score++;
			}
			if (ox[j] == 'X')
			{
				score = 1;
			}
		}	printf("%d\n", sum);
	}
	return 0;
}