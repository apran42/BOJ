#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int stack[10001] = { 0, };
int cnt = -1;

void push(int x);
void pop();
void size();
void empty();
void top();


int main() {
    char order[10];
    int n, x = 0;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%s", order);

        if (!strcmp(order, "push")) {
            scanf("%d", &x);
            push(x);
        }

        if (!strcmp(order, "pop")) {
            pop();
        }

        if (!strcmp(order, "size")) {
            size();
        }

        if (!strcmp(order, "empty")) {
            empty();
        }

        if (!strcmp(order, "top")) {
            top();
        }
    }
    return 0;
}

void push(int x) {
    int i = 0;
    while (1) {
        if (stack[i] != 0)
            i++;
        else {
            stack[i] = x;
            break;
        }
    }
    cnt++;
}

void pop() {
    if (cnt != -1) {
        printf("%d\n", stack[cnt]);
        stack[cnt] = 0;
        cnt--;
    }
    else
        puts("-1");

}

void size() {
    printf("%d\n", cnt + 1);
}

void empty() {
    if (stack[0] == 0)
        puts("1");
    else
        puts("0");
}

void top() {
    if (stack[cnt] != 0)
        printf("%d\n", stack[cnt]);
    else
        puts("-1");
}