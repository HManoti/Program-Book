#include <iostream>
using namespace std;

struct Node {
  int data;
  Node* left;
  Node* right;
};

int countLeafNodes(Node* root) {
  if (root == NULL)
    return 0;
  if (root->left == NULL && root->right == NULL)
    return 1;
  else
    return countLeafNodes(root->left) + countLeafNodes(root->right);
}

int main() {
  Node* root = new Node(1);
  root->left = new Node(2);
  root->right = new Node(3);
  root->left->left = new Node(4);
  root->left->right = new Node(5);

  int count = countLeafNodes(root);
  cout << "The number of leaf nodes is " << count << endl;

  return 0;
}