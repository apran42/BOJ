#include <stdio.h>
#include <string.h>

char arr[1000000] = { 0, };

int main()
{
	char count[26] = { 0, };
	scanf("%s", arr, 1000000);
	int chk[26] = { 0, };
	for (int i = 0; i < 26; i++)
	{
		count[i] = (char)(i + 65);
	}

	for (int i = 0; i < 26; i++)
	{
		for (int j = 0; j < sizeof(arr); j++)
		{
			if (arr[j]==count[i] || arr[j]==count[i]+32)
			{
				chk[i]++;
			}
		}
	}

	int a = 0;
	int tmp = 0;
	for (int i = 0; i < 26; i++)
	{
		if (chk[i] > a)
			a = chk[i];
	}

	for (int i = 0; i < 26; i++)
	{
		if (chk[i] == a)
			tmp++;
	}

	if (tmp != 1)
		printf("?");
	else
		for (int i = 0; i < 26; i++)
		{
			if (chk[i] == a)
				printf("%c", count[i]);
		}

	return 0;
}