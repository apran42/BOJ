#include <stdio.h>
int main() {
	int t = 0; int count = 0;
	int h, w, n = 0;
	scanf("%d", &t);
	for (int i = 0; i < t; i++)
	{
		scanf("%d %d %d", &h, &w, &n);
		count=hcount(h,w,n);
		printf("%d\n", count);
	}


	return 0;
}

int hcount(int h,int w,int n) {
	int result = 0;
	int count = 1;
	while (1)
	{
		if (h < n)
		{
			count++;
			n -= h;
		}
        else
            break;
	}
	result = n * 100 + count;

	return result;
}