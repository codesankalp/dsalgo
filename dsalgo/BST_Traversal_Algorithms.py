“””  Binary Search Tree : tree where parent has two child nodes and left child node value is less than Root/parent and right child node value is greater than parent.

Binary Search Tree Traversal Algorithms
    1. Preorder Traversal
    2. Postorder Traversal
    3. Inorder Traversal

self.right : right child node of the parent node
self.left : left child node of the parent node
self.info = value of node
“””


class Node:
	def __init__(self, info):
		self.left = left 
		self.right = right
		self.info = info

	def __str__(self):
		return str(self.info)

class BinarySearchTree:
	def __init__(self):
		self.root = None
	
	def create(self, val):
		 if self.root = None:
			self.root= Node(val)
		else:
			cur = self.root
			while True:
				if val < cur.info:
					if cur.left:
						cur = cur.left
					else:
						cur.left = Node(val)
						break
				elif val >  cur.info:
					if cur.right:
						cur = cur.right
					else:
						cur.right = Node(val)
						break	
				else:
					break

“”” 
Preorder traversal follows: Root/parent node——>left child node——>right child node , I.e first root/ parent node is visited then left child node is visited and finally right child node 

“””

def preorder(root):
	if root:
		print(root.info)
		preorder(root.left)
		preorder(root.right)

“”” 
Postorder traversal follows: left child node——>right child node ——> Root/parent node, I.e first  left child node is visited then right child node is visited and finally root/ parent node

“””

def postorder(root):
	if root:
		postorder(root.left)
		postorder(root.right)
		print(root.info)


“”” 
Inorder traversal follows: left child node——> Root/parent node——> right child node, I.e first  left child node is visited then root/ parent node is visited and finally right child node 

“””

def inorder(root):
	if root:
		postorder(root.left)
		print(root.info)
		postorder(root.right)

tree =  BinarySearchTree()

l = int(input())

arr = list(map(int, input().split()))

for i in range(l):
	tree.create(arr[i])


preorder(tree.root)
postorder(tree.root)
inorder(tree.root)
		

	

