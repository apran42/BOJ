#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int cmp(const void* a, const void* b) {
	// 길이가 다름
	if (strlen(*(const char**)a) > strlen(*(const char**)b)) return 1;
	else if (strlen(*(const char**)a) < strlen(*(const char**)b)) return -1;
	
	// 길이가 같음
	else return strcmp(*(const char**)a, *(const char**)b);	
}

int main() {
	int n;
	scanf("%d", &n);

	char** words = (char**)malloc(sizeof(char*) * n);

	for (int i = 0; i < n; i++) {
		words[i] = (char*)malloc(sizeof(char) * 51);
		scanf("%s", words[i]);
	}

	qsort(words, n, sizeof(char*), cmp);

	for (int i = 0; i < n; i++) {
		if (i == n - 1 || strcmp(words[i], words[i + 1]) != 0)
			printf("%s\n", words[i]);
	}
	free(words);

	return 0;
}