#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		char ps[51];
		int lp = 0, rp = 0;
		scanf("%s", ps);
		ps[strlen(ps)] = '\0';
		for (int j = 0; j < (int)strlen(ps); j++) {
			if (ps[j] == '(')
				lp++;
			else {
				if (lp != 0)
					lp--;
				else {
					rp++;
					break;
				}
			}
		}
		if (lp == 0 && rp == 0)
			puts("YES");
		else
			puts("NO");
	}
	return 0;
}
