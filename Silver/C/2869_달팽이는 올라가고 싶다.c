#include <stdio.h>

int main() {
	int a, b, v;
	scanf("%d %d %d", &a, &b, &v);
	if (a == v)
	{
		printf("%d", 1);
		return 0;
	}
	int day = a - b; 
	int d = v - a; 
	int fin;
	if (d % day != 0) fin = d / day + 1;
	else fin = d / day;
	printf("%d", fin + 1);
	return 0;
}