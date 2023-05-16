#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct _Node {
	int data;
	struct _Node* next;
}Node;

typedef struct _Queue {
	Node* front;
	Node* rear;
	int size;
}Queue;

void init(Queue* queue) {
	queue->front = NULL;
	queue->rear= NULL;
	queue->size = 0;
}

void push(Queue* queue, int data) {
	Node* newNode = (Node*)malloc(sizeof(Node));
	newNode->data = data;
	newNode->next = NULL;

	// 큐가 빈 경우
	if (queue->rear == NULL) {
		queue->front = newNode;
		queue->rear = newNode;
	}
	else {
		queue->rear->next = newNode;
		queue->rear = newNode;
	}

	queue->size++;
}

void pop(Queue* queue) {
	if (queue->front == NULL) {
		printf("-1\n");
		return;
	}
	Node* tmp = queue->front;
	queue->front = queue->front->next;
	queue->size--;

	if (queue->front == NULL)
		queue->rear = NULL;
	printf("%d\n", tmp->data);
	free(tmp);
}

void front(Queue* queue) {
	if (queue->front == NULL) {
		printf("-1\n");
		return;
	}
	else
		printf("%d\n", queue->front->data);
}

void back(Queue* queue) {
	if (queue->rear == NULL) {
		printf("-1\n");
		return;
	}
	else
		printf("%d\n", queue->rear->data);
}

int main() {
	Queue queue;
	init(&queue);

	int n,x;
	char comment[6] = { '\0', };
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%s", comment);
		if (!strcmp(comment, "push")) {
			scanf("%d", &x);
			push(&queue, x);
		}
		else if (!strcmp(comment, "pop"))
			pop(&queue);
		else if (!strcmp(comment, "size"))
			printf("%d\n", queue.size);
		else if (!strcmp(comment, "empty")) {
			if (queue.size > 0)
				printf("0\n");
			else
				printf("1\n");
		}
		else if (!strcmp(comment, "front"))
			front(&queue);
		else if (!strcmp(comment, "back"))
			back(&queue);
	}
}