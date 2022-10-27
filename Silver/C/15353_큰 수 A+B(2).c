#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char num1[10000] = { '0', };
char num2[10000] = { '0', };
char res[10001] = { '0', };

void reverse(char* a)
{
	int temp, len = strlen(a);

	for (int i = 0; i < len / 2; i++)
	{
		temp = a[i];
		a[i] = a[len - i - 1];
		a[len - i - 1] = temp;
	}
}

int main()
{
	int len = 0, tmp = 0, tmp1 = 0;
	scanf("%s %s", num1, num2);
	
	reverse(num1);
	reverse(num2);

	if (strlen(num1) >= strlen(num2))
	{
		len = strlen(num1);
	}
	else
	{
		len = strlen(num2);
	}

	for (int i = 0; i < len; i++)
	{
		tmp = ((int)num1[i] - 48) + ((int)num2[i] - 48) + tmp1;
		if (tmp < 0)
		{
			tmp += 48;
		}
		if (tmp >= 10)
		{
			tmp1 = 1;
		}
		else
		{
			tmp1 = 0;
		}
		res[i] = (tmp % 10) + 48;
	}

	if (tmp1 == 1)
	{
		res[len] = (char)49;
	}

	reverse(res);
	printf("%s", res);

	//system("pause");
	return 0;
}