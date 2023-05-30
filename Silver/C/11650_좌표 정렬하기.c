#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct _Point {
	int x;
	int y;
}Point;

int compare(void* a, void* b) {
	Point tmp_a = *(Point*)a;
	Point tmp_b = *(Point*)b;

	if (tmp_a.x > tmp_b.x) {
		// X 좌표가 클 때
		return 1;
	}
	// X좌표가 같을 때
	else if (tmp_a.x == tmp_b.x) {
		// Y좌표가 크다면
		if (tmp_a.y > tmp_b.y)
			return 1;
		// 그게 아니라면
		else
			return -1;
	}
	// X좌표가 작을 때
	else
		return -1;
}

int main() {
	int n;
	scanf("%d", &n);
	Point* points = (Point*)malloc(sizeof(Point) * n);
	
	for (int i = 0; i < n; i++)
		scanf("%d %d", &points[i].x, &points[i].y);

	qsort(points, n, sizeof(Point), compare);

	for (int i = 0; i < n; i++)
		printf("%d %d\n", points[i].x, points[i].y);

	free(points);
}