#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

typedef struct _Node {
	int data;
	struct _Node* next;
}Node;

typedef struct _Queue {
	Node* front;
	Node* rear;
	int size;
}Queue;

void init(Queue* q) {
	q->front = NULL;
	q->rear = NULL;
	q->size = 0;
}

void push(Queue* head, int data) {
	Node* tmpNode = (Node*)malloc(sizeof(Node));
	tmpNode->data = data;
	tmpNode->next = NULL;
	if (head->rear == NULL) {
		head->front = tmpNode;
		head->rear = tmpNode;
		tmpNode->next = tmpNode;
	}
	else {
		head->rear->next = tmpNode;
		head->rear = tmpNode;
		tmpNode->next = head->front;
	}
	head->size++;
}


int main() {
	Queue josephus;
	init(&josephus);

	int n, k, t;
	scanf("%d %d", &n, &k);

	for (int i = 0; i < n; i++) {
		push(&josephus, (i + 1));
	}
	Queue cur;
	cur.front = josephus.rear;

	printf("<");

	while (n != 0) {
		t = k;
		while (t != 0) {
			cur.front = cur.front->next;
			if (cur.front->data != 0)
				t--;
		}
		if (n != 1)
			printf("%d, ", cur.front->data);
		else
			printf("%d>", cur.front->data);
		cur.front->data = 0;
		n--;
	}
}
