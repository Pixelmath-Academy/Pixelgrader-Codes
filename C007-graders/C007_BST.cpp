#include <bits/stdc++.h>
using namespace std;

struct Node {
    int key;
    Node* left;
    Node* right;
    Node(int k) : key(k), left(nullptr), right(nullptr) {}
};

class BST {
public:
    BST() : root(nullptr) {}

    void insert(int key) {
        root = insertRec(root, key);
    }

    bool find(int key) {
        return findRec(root, key);
    }

    void print() {
        preOrder(root);
        cout << endl;
    }

private:
    Node* root;

    Node* insertRec(Node* node, int key) {
        if (node == nullptr) {
            return new Node(key);
        }
        if (key < node->key) {
            node->left = insertRec(node->left, key);
        } else if (key > node->key) {
            node->right = insertRec(node->right, key);
        }
        return node;
    }

    bool findRec(Node* node, int key) {
        if (node == nullptr) {
            return false;
        }
        if (node->key == key) {
            return true;
        }
        if (key < node->key) {
            return findRec(node->left, key);
        } else {
            return findRec(node->right, key);
        }
    }

    void preOrder(Node* node) {
        if (node == nullptr) {
            return;
        }
        cout << node->key << " ";
        preOrder(node->left);
        preOrder(node->right);
    }
};

int main() {
    int n;
    cin >> n;
    BST tree;
    for (int i = 0; i < n; ++i) {
        string command;
        int k;
        cin >> command;
        if (command == "insert") {
            cin >> k;
            tree.insert(k);
        }
        else if (command == "find") {
            cin >> k;
            if (tree.find(k)) {
                cout << "YES" << endl;
            } else {
                cout << "NO" << endl;
            }
        }
        else if (command == "print") {
            tree.print();
        }
    }
    return 0;
}
