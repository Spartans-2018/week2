




class Node:
	""" Get and provide current node and next node """

	def __init__(self, node, next_node = None):
		self.node = node
		self.next_node = next_node

	def get_next(self):
		return self.next_node

	def set_next(self, next):
		self.next_node = next_node

	def get_node(self):
		return self.node

	def set_node(self, node):
		self.node = node



class Linked_List:
	""" find size of linked list and find, add, remove nodes """

	def __init__(self, root = None):
		self.root = root
		self.size = 0

	def get_size(self):
		""" add or remove from count of nodes """
		print ("get size: ", self.size)
		return self.size
		

	def add(self, node):
		""" append new node to beginning of linked list and add 1 to size """

		new_node = Node(node, self.root) # set new 
		self.root = new_node # set new node to root
		self.size += 1
		print ("added size: ", self.size)


	def remove(self,node):
		""" find input node and set previous node pointer to next node, skipping input node """

		this_node = self.root
		prev_node = None
		
		while this_node:
			print ('while this node')

			if this_node.get_node() == node: # if match is found

				if prev_node: # if a previous node exists
					prev_node.set_next(this_node.get_next()) # set previous pointer to next node
				else:
					print ("no prev node")
					self.root = this_node # determine if input node is first
				self.size -= 1
				print ("removed size: ", self.size)
				return True
			else:
				prev_node = this_node
				this_node = this_node.get_next()
		return False

	def find(self,node):
		""" iterate through the list of lists """

		this_node = self.root # set beginning of search
		while this_node:
			if this_node.get_node() == node:
				print ('find this node: ', node)
				return node
			else:
				self.root = this_node.get_next()
				print ('root: ', self.root)
		return None





my_nodes = Linked_List()

my_nodes.add(7)
my_nodes.add(9)
my_nodes.add(15)
print (my_nodes.remove(15))

print(my_nodes.find(15))











#insert
#search (First iteratively then recursively)
#delete
#print backwards