#include <stdio.h>

int arr[10000] = { 0 };

int main()
{
	for (int i = 0; i < 10000; i++)
	{
		arr[i] = i + 1;	
	}

	for (int i = 0; i < 10000; i++)
	{
		arr[s_n(i + 1) - 1] = 0;
	}

	for (int i = 0; i < 10000; i++)
	{
		if (arr[i] != 0)
		{
			printf("%d\n", arr[i]);
		}
	}

	return 0;

}
int s_n(int n)
{
	int a, b, c, d = 0;
	a = n / 1000;		
	b = n % 1000 / 100;	
	c = n % 100 / 10;	
	d = n % 10;			
	n += (a + b + c + d);

	return n;
}