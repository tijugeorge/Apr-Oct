#linkedlist basics


#node class
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

#linkedlist class to intialize the node object
class LinkedList:
	def __init__(self):
		self.head = None

	def printList(self):
		temp = self.head
		while temp:
			print(temp.data, end = " ")
			temp = temp.next

#code execution
if __name__ == '__main__':
	llist = LinkedList()
	llist.head = Node(1)
	second = Node(2)
	third = Node(3)
	llist.head.next = second
	second.next = third

	llist.printList()

