#include <stdio.h>
#include <string.h>

int main()
{
	int count = 0, tmp = 0;
	int a;
	char arr1[21];
	scanf("%d", &count);
	for (int i = 0; i < count; i++)
	{
		scanf("%d", &a);
		scanf("%s", arr1);
		char arr2[200] = "";
        tmp = 0;
		if (a >= 1 && a <= 8)
		{
			if (strlen(arr1) <= 20)
			{
				for (int j = 0; j < strlen(arr1); j++)
				{
					for (int k = 0; k < a; k++)
					{
						arr2[tmp] = arr1[j];
						tmp++;
					}
				}

			}
		}
		else if (a > 8)
		{
			a = 8;

			if (strlen(arr1) <= 20)
			{
				for (int j = 0; j < strlen(arr1); j++)
				{
					for (int k = 0; k < a; k++)
					{
						arr2[tmp] = arr1[j];
						tmp++;
					}
				}

			}
		}
		else
		{
			a = 1;

			if (strlen(arr1) <= 20)
			{
				for (int j = 0; j < strlen(arr1); j++)
				{
					for (int k = 0; k < a; k++)
					{
						arr2[tmp] = arr1[j];
						tmp++;
					}
				}

			}
		}
		printf("%s\n", arr2);
	}

	return 0;
}