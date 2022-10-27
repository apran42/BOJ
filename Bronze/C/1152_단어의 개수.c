#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

char arr[1000000];

int main()
{
	int word = 1;
	scanf("%[^\n]s", arr, 1000000);
	for (int i = 0; i < strlen(arr); i++)
	{
		if (arr[i] == ' ')
			word++;
	}

	if (arr[0] == ' ')
		word -= 1;
	if (arr[strlen(arr) - 1] == ' ')
		word -= 1;

	printf("%d", word);
	
	return 0;
}