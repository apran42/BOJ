#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {
	int n, chk = 0, chk2;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		char word[101];
		scanf("%s", word);
		chk2 = 0;
		for (int j = 1; j < (int)strlen(word); j++) {
			if (word[j] != word[j - 1]) {
				for (int k = 0; k < j; k++) {
					if (word[k] == word[j] && chk2 == 0) {
						chk++;
						chk2++;
					}
				}
			}
		}
	}
	printf("%d", n - chk);
}