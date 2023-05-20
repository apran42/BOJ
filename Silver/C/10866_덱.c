#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct _Node {
	int data;
	struct _Node* next;
	struct _Node* prev;
}Node;

typedef struct _Deque {
	Node* front;
	Node* rear;
	int size;
}Deque;

void init(Deque* deque) {
	deque->front = NULL;
	deque->rear = NULL;
	deque->size = 0;
}

void push_back(Deque* deque, int data) {
	Node* tmpNode = (Node*)malloc(sizeof(Node));
	tmpNode->next = NULL;
	tmpNode->prev = NULL;
	tmpNode->data = data;

	// 처음 삽입
	if (deque->rear == NULL) {
		deque->rear = tmpNode;
		deque->front = tmpNode;
	}
	else {
		deque->rear->next = tmpNode;
		tmpNode->prev = deque->rear;
		deque->rear = tmpNode;
	}
	deque->size++;
}

void push_front(Deque* deque, int data) {
	Node* tmpNode = (Node*)malloc(sizeof(Node));
	tmpNode->next = NULL;
	tmpNode->prev = NULL;
	tmpNode->data = data;

	// 처음 삽입
	if (deque->front == NULL) {
		deque->rear = tmpNode;
		deque->front = tmpNode;
	}
	else {
		deque->front->prev = tmpNode;
		tmpNode->next = deque->front;
		deque->front = tmpNode;
	}
	deque->size++;
}

void pop_front(Deque* deque) {
	if (deque->size == 0) {
		printf("-1\n");
		return;
	}
	else {
		Node* tmp = deque->front;
		if (deque->size == 1) {
			printf("%d\n", tmp->data);
			free(tmp);
			deque->front = NULL;
			deque->rear = NULL;
		}
		else {
			deque->front = tmp->next;
			tmp->next->prev = NULL;
			tmp->next = NULL;
			printf("%d\n", tmp->data);
			free(tmp);
		}
		deque->size--;
	}
}

void pop_back(Deque* deque) {
	if (deque->size == 0) {
		printf("-1\n");
		return;
	}
	else {
		Node* tmp = deque->rear;
		if (deque->size == 1) {
			printf("%d\n", tmp->data);
			free(tmp);
			deque->front = NULL;
			deque->rear = NULL;
		}
		else {
			deque->rear = tmp->prev;
			tmp->prev->next = NULL;
			tmp->prev = NULL;
			printf("%d\n", tmp->data);
			free(tmp);
		}
		deque->size--;
	}
}

void front(Deque* deque) {
	if (deque->size == 0) {
		printf("-1\n");
		return;
	}
	else {
		printf("%d\n", deque->front->data);
	}
}

void back(Deque* deque) {
	if (deque->size == 0) {
		printf("-1\n");
		return;
	}
	else {
		printf("%d\n", deque->rear->data);
	}
}

int main() {
	Deque deque;
	init(&deque);

	int n, x;

	scanf("%d%*c", &n); // 입력 버퍼에서 개행문자 제거

	for (int i = 0; i < n; i++) {
		char command[11] = { '\0', };
		scanf("%s", command);
		if (!strcmp(command, "push_front")) {
			scanf("%d", &x);
			push_front(&deque, x);
		}
		else if (!strcmp(command, "push_back")) {
			scanf("%d", &x);
			push_back(&deque, x);
		}
		else if (!strcmp(command, "pop_front"))
			pop_front(&deque);
		else if (!strcmp(command, "pop_back"))
			pop_back(&deque);
		else if (!strcmp(command, "size"))
			printf("%d\n", deque.size);
		else if (!strcmp(command, "empty")) {
			if (deque.size == 0)
				printf("1\n");
			else
				printf("0\n");
		}
		else if (!strcmp(command, "front"))
			front(&deque);
		else if (!strcmp(command, "back"))
			back(&deque);		
	}
}