#include <stdio.h>
#include <stdlib.h>

int main()
{
	char s[100] = { 'null', };
	scanf("%s", s);
	
	int res[26] = {0};

	for (int i = 0; i < 26; i++)
	{
		res[i] = -1;
	}

	for (int i = 0; i < 100; i++)		// 최대 문자 개수
	{
		for (int k = i+1; k < 100; k++)
		{
			if (s[i] == s[k])
			{
				s[k] = 0;
			}
		}

		for (int j = 0; j < 26; j++)	// 알파벳 개수
		{
			if ((int)s[i] == j + 97)
			{
				res[j] = i;
			}
			
		}
	}

	for (int i = 0; i < 26; i++)
	{
		printf("%d ", res[i]);
	}

	return 0;
}