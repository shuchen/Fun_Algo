import bst

def height(node):
	if node is None:
		return -1
	else:
		return node.height
		
def update_height(node):
	node.height = max(height(node.left), height(node.right)) + 1
	
class AVL(bst.BST):
"""
AVL binary search tree implementation. 
Supports insert, find, and delete-min operations in O(lg n) time
"""
	def left_rotate(self, x):
	
	def right_rotate(self.x):
	
	def insert(self, t):
	
	def rebalance(self, node):
	
	def delete_min(self):
	
def test(args=None):

if __name__ == '__main__': test()