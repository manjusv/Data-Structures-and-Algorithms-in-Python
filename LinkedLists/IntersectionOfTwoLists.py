# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-03 16:45:30
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-01-03 17:21:55
class ListNode:
	def __init__(self, data):
		self.val = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	# Function to find length of list
	def Len(self, head):
		temp = head
		len = 0
		while(temp):
			len += 1
			temp = temp.next
		return len

	# get Intersection Node
	def getIntersectionNode(self, head1, head2, d):
		cur1 = head1
		cur2 = head2
		# Since len of list pointed by list1 is bigger, traverse that list by d nodes
		while(d != 0):
			cur1 = cur1.next
			d -= 1
		# Now both lists have same length starting from cur1 and cur2
		while(cur1 and cur2):
			if(cur1 == cur2):
				return cur1
			cur1 = cur1.next
			cur2 = cur2.next
		# If there is no intersection return None
		return None 

	# Function to reverse the linkedlist
	def Intersection(self, head1, head2):
		cur1 = head1
		cur2 = head2
		# find length of list1
		len1 = self.Len(head1)
		# find length of list2
		len2 = self.Len(head2)

		if(len1 >= len2):
			d = len1 - len2
			return self.getIntersectionNode(head1, head2, d)
		d = len2 - len1
		return self.getIntersectionNode(head2, head1, d)

	# insert a new element at the beginning of a list
	def push(self, new_data):
		new_node = ListNode(new_data)
		new_node.next = self.head
		self.head = new_node

	# prints the contents of a list
	def printList(self):
		temp = self.head
		while(temp):
			print temp.val,
			temp = temp.next

llist1 = LinkedList()
llist1.push(5)
llist1.push(4)
llist1.push(3)
llist1.push(2)
llist1.push(1)

llist2 = LinkedList()
llist2.push(7)
llist2.push(8)

llist2.head.next.next = llist1.head.next.next
print "LinkedList1  : ", llist1.printList()
print "LinkedList2  : ", llist2.printList()

print "Intersecting Node is : ", llist1.Intersection(llist1.head, llist2.head).val

