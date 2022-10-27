#include <stdio.h>
#include <string.h>

int main()
{
	int cnt = 0;
	
	char array[100]={ };
	scanf("%s", array);
	for	(int i = 0; i < strlen(array); i++)
	{
		if ((array[i] == 'c' && array[i + 1] == '-') || (array[i] == 'c' && array[i + 1] == '=') ||
			(array[i] == 'd' && array[i + 1] == '-') || (array[i] == 'l' && array[i + 1] == 'j') ||
			(array[i] == 'n' && array[i + 1] == 'j') || (array[i] == 's' && array[i + 1] == '=') ||
			(array[i] == 'z' && array[i + 1] == '='))
			{
				cnt++;
				i++;
			}
		else if (array[i] == 'd' && array[i + 1] == 'z' && array[i + 2] == '=')
			{
				cnt++;
				i += 2;
			}
		else
			cnt++;
	}
	printf("%d", cnt);
	
	return 0;
}