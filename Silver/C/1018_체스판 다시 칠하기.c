#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int check(char** input_data, char** board1, char** board2, int a, int b) {
	int cnt1 = 0, cnt2 = 0;
	for (int i = a; i < a + 8; i++) {
		for (int j = b; j < b + 8; j++) {
			if (input_data[i][j] != board1[i % 8][j % 8])
				cnt1++;
			if (input_data[i][j] != board2[i % 8][j % 8])
				cnt2++;
		}
	}
	return (cnt1 < cnt2) ? cnt1 : cnt2;
}

int main() {
	char** board1 = (char**)malloc(sizeof(char*) * 8);
	char** board2 = (char**)malloc(sizeof(char*) * 8);
	for (int i = 0; i < 8; i++) {
		board1[i] = (char*)malloc(sizeof(char) * 8);
		board2[i] = (char*)malloc(sizeof(char) * 8);
		if (i % 2 == 0) {
			board1[i] = "WBWBWBWB";
			board2[i] = "BWBWBWBW";
		}
		else {
			board1[i] = "BWBWBWBW";
			board2[i] = "WBWBWBWB";
		}
	}

	int n, m;
	scanf("%d %d", &n, &m);
	char** input_data = (char**)malloc(sizeof(char*) * n);
	for (int i = 0; i < n; i++) {
		input_data[i] = (char*)malloc(sizeof(char) * m);
		scanf("%s", input_data[i]);
	}

	int res = 64;

	for (int i = 0; i < (n - 7); i++) {
		for (int j = 0; j < (m - 7); j++) {
			int tmp = check(input_data, board1, board2, i, j);
			if (tmp < res)
				res = tmp;
		}
	}

	printf("%d", res);

	free(board1);
	free(board2);
	free(input_data);

	return 0;
}