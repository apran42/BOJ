#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {
	char word[101];
	scanf("%s", word);
	int len = strlen(word);
	int tmp = -1;
	for (int i = 0; i < len / 2; i++) {
		if (word[i] != word[len + tmp--]) {
			printf("0");
			return 0;
		}
		else
			continue;
	}
	printf("1");
}