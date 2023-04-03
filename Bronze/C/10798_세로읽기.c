#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	char board[5][16] = { "", };
	for (int i = 0; i < 5; i++)
		scanf("%s", board[i]);
	for (int j = 0; j < 15; j++) {
		for (int k = 0; k < 5; k++) {
			int asc = (int)board[k][j];
			if (asc >= 97 && asc <= 122 || asc >= 65 && asc <= 90 || asc >= 48 && asc <= 57)
				printf("%c", board[k][j]);
		}
	}
}