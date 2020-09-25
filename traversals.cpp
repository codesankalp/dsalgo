struct Node {
	int val;
	Node* left;
	Node* right;
	Node() {
		left=NULL;
		right=NULL;
	}
}
void inorder_traversal(Node * root) {
	if(root==NULL)
		return;

	inorder_traversal(root->left);
	cout<<root->val;
	inorder_traversal(root->right);
}

void preorder_traversal(Node * root) {
	if(root==NULL)
		return;

	cout<<root->val;
	preorder_traversal(root->left);
	preorder_traversal(root->right);
}

void postorder_traversal(Node * root) {
	if(root==NULL)
		return;
	postorder_traversal(root->left);
	postorder_traversal(root->right);
	cout<<root->val;
}
