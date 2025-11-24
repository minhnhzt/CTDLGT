#include <iostream>
using namespace std;

struct Node {
    float data;
    Node* next;
    Node(float val) : data(val), next(nullptr) {}
};

int listLength(Node* head) {
    int length = 0;
    Node* current = head;
    while (current != nullptr) {
        length++;
        current = current->next;
    }
    return length;
}

void printList(Node* head) {
    Node* current = head;
    while (current != nullptr) {
        cout << current->data << " -> ";
        current = current->next;
    }
    cout << "nullptr" << endl;
}

void appendNode(Node** head_ref, int new_data) {
    Node* new_node = new Node(new_data);
    if (*head_ref == nullptr) {
        *head_ref = new_node;
        return;
    }
    Node* last = *head_ref;
    while (last->next != nullptr) {
        last = last->next;
    }
    last->next = new_node;
}

int main() {
    Node* head = nullptr;

    appendNode(&head, 2.5);
    appendNode(&head, 2.8);
    appendNode(&head, 3.3);

    cout << "Linked List: ";
    printList(head);

    cout << "Length of Linked List: " << listLength(head) << endl;
    while (head != nullptr) {
        int i = 0;
        if (head -> data > 3.2) {
            i++;
        }
        cout << "SV co GPA cao hon 3.2: " << i << endl;
        head = head->next;
    }
    return 0;
}
