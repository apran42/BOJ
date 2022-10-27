#include <stdio.h>
int main() {
	int x, y, w, h;
	scanf("%d %d %d %d", &x, &y, &w, &h);
	int res = w; int arr[4] = { x, y, w - x, h - y };
	for (int i = 0; i < 4; i++)
	{
		if (arr[i] < res) res = arr[i];
	}
	printf("%d", res);
}