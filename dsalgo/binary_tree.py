class node:
	def __init__(self,value=None):
		self.value=value
		self.left_child=None
		self.right_child=None

class binary_search_tree:
	def __init__(self):
		self.root=None

	def insert(self,value):
		if self.root==None:
			self.root=node(value)
		else:
			self._insert(value,self.root)

	def _insert(self,value,cur_node):
		if value<cur_node.value:
			if cur_node.left_child==None:
				cur_node.left_child=node(value)
			else:
				self._insert(value,cur_node.left_child)
		elif value>cur_node.value:
			if cur_node.right_child==None:
				cur_node.right_child=node(value)
			else:
				self._insert(value,cur_node.right_child)
		else:
			print("Value already in tree!")     

	def search(self,value):
		if self.root!=None:
			return self._search(value,self.root)
		else:
			return False

	def _search(self,value,cur_node):
		if value==cur_node.value:
			return True
		elif value<cur_node.value and cur_node.left_child!=None:
			return self._search(value,cur_node.left_child)
		elif value>cur_node.value and cur_node.right_child!=None:
			return self._search(value,cur_node.right_child)      

def fill_tree(tree,num_element=10,max_int=100):
    from random import randint
    for i in range(num_element):
        cur_element=randint(0,max_int)
        tree.insert(cur_element)
    return tree

tree = binary_search_tree()    

n = int(input('Number of Elements: '))
for i in range(n):
    value=int(input('Enter Element: '))
    tree.insert(value)
s = int(input('Search Element: '))
print(tree.search(s))