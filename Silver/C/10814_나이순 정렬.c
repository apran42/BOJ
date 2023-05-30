#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Member {
	int age;
	char name[201];
}Member;

int compare(void* p, void* q) {
	Member mp = *(Member*)p;
	Member mq = *(Member*)q;

	if (mp.age > mq.age)
		return 1;
	else
		return -1;
}

int main() {
	int n;
	scanf("%d", &n);
	Member* members = (Member*)malloc(sizeof(Member) * n);
	
	for (int i = 0; i < n; i++)
		scanf("%d %s", &members[i].age, members[i].name);

	qsort(members, n, sizeof(Member), compare);

	for (int i = 0; i < n; i++)
		printf("%d %s\n", members[i].age, members[i].name);
	
	free(members);
}