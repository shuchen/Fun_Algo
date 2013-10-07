class BST(object):
"""
Simple binary search tree class implementation
insert
find
delete-min
"""

	def __init__(self):
		self.root = None
		
	def insert(self, t):
	
	def find(self, t):
	
	def delete_min(self):
	
	def __str__(self):
	
class BSTnode(object):
"""
Binary search tree node class.
Contains a left child, right child and key value
"""
	
	def __init__(self, t):
	"""Create a new leaf with t."""
		self.key = t
		self.disconnect()
		
	def disconnect(self):
		self.left = None
		self.right = None
		self.parent = None
		
def test(args=None, BSTtype=BST):
	
if __name__ == '__main__': test()
	