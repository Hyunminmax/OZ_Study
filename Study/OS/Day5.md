# 연결리스트 Linked List
각 데이터 항목을 노드라는 구조료 표현 하고 각 노드는 데이터를 포함하고 다음 노드를 가리키는 참조를 포함한다. 

통신에서 각 데이터 패킷의 헤더 부분에 각종 실제 데이터가 아닌 접속정보등 여러 정보를 담고 있듯 연결리스트 자료형의 노드는 다음 노드의 위치 값을 가지고 있다. 

이 위치 값을 가지고 있는 방식에 따라 3가지 연결리스트 자료형으로 구분된다. 
1. 단일 : 가장 간단한 형식으로 다음 노드의 위치를 가리킨다.
2. 이중 : 이전 노드와 다음 노드의 위치를 모두 가리키고 있어 양방향 탐색이 가능하다. 
3. 원형 : 마지막 노드가 첫 번째 노드의 위치를 가리키고 있어 순환 구조를 가진다. 


```
#include <stdio.h>
#include <stdlib.h>

// 연결 리스트의 노드 구조 정의
typedef struct Node {
    int data;
    struct Node* next;
} Node;

// 연결 리스트 초기화
Node* createNode(int data) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    if (newNode == NULL) {
        fprintf(stderr, "메모리 할당 에러\n");
        exit(1);
    }
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// 연결 리스트에 노드 추가
void append(Node** head, int data) {
    Node* newNode = createNode(data);
    if (*head == NULL) {
        *head = newNode;
    } else {
        Node* current = *head;
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = newNode;
    }
}

// 연결 리스트 출력
void display(Node* head) {
    Node* current = head;
    while (current != NULL) {
        printf("%d -> ", current->data);
        current = current->next;
    }
    printf("NULL\n");
}

int main() {
    Node* head = NULL;  // 연결 리스트의 헤드 초기화
    append(&head, 1);   // 리스트에 요소 추가
    append(&head, 2);
    append(&head, 3);
    display(head);      // 연결 리스트 출력
    return 0;
}
```