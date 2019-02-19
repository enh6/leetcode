/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() {}

    Node(int _val, Node* _left, Node* _right, Node* _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/
class Solution {
public:
    Node* connect(Node* root) {
        Node* node = root;
        Node* head = nullptr;
        Node* tail = nullptr;
        while (node) {
            if (node->left) {
                if (tail) {
                    tail->next = node->left;
                    tail = tail->next;
                } else {
                    head = tail = node->left;
                }
            }
            if (node->right) {
                if (tail) {
                    tail->next = node->right;
                    tail = tail->next;
                } else {
                    head = tail = node->right;
                }
            }
            if (node->next) {
                node = node->next;
            } else {
                node = head;
                head = tail = nullptr;
            }
        }
        return root;
    }
};
