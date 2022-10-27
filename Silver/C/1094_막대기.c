#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int makdaegi(int a);

int main()
{
	int x = 0;
	scanf("%d", &x);

	x = makdaegi(x);

	printf("%d", x);

	return 0;
}

int makdaegi(int x)
{
	int cnt = 0;

	if (x >= 64)
	{
		x -= 64;
		cnt++;
	}
	if (x >= 32)
	{
		x -= 32;
		cnt++;
	}
	if (x >= 16)
	{
		x -= 16;
		cnt++;
	}
	if (x >= 8)
	{
		x -= 8;
		cnt++;
	}
	if (x >= 4)
	{
		x -= 4;
		cnt++;
	}
	if (x >= 2)
	{
		x -= 2;
		cnt++;
	}
	if (x == 1)
		cnt++;

	return cnt;
}