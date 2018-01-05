# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-05 16:19:20
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-01-05 17:04:11

# given two sorted LinkedLists, Merge them to get a new sorted linked list
class ListNode:
	def __init__(self, data):
		self.val = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	# Function to Merge two sorted linkedlists
	def MergeTwoSortedLinkedLists(self, head1, head2):
		# if head is None return
		if head1 == None:
			return head2
		if head2 == None:
			return head1

		# create a new result linkedlist
		result = LinkedList()

		while head1 or head2:
			if head1.val == head2.val:
				result.push(head1.val)
				result.push(head2.val)
				head1 = head1.next
				head2 = head2.next
			elif head1.val < head2.val:
				result.push(head1.val)
				head1 = head1.next
			else:
				result.push(head2.val)
				head2 = head2.next

		# check if both head1 and head2 became null
		if head1 == None and head2 == None:
			return result

		# Now check if either of list1 or list2 became null
		if head1 == None:
			while(head2):
				result.push(head2.val)
				head1 = head2.next
			return result

		if head2 == None:
			while(head1):
				result.push(head1.val)
				head1 = head1.next
			return result


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

# create a linked list with user input
llist1 = LinkedList()
n = input("Enter the number of elements in LinkedList 1 : ")
print "Enter elements : "
for i in range(0, n):
	llist1.push(input())

llist2 = LinkedList()
n = input("Enter the number of elements in LinkedList 2: ")
print "Enter elements : "
for i in range(0, n):
	llist2.push(input())

print "Input LinkedList 1 : ", llist1.printList()
print "Input LinkedList 2 : ", llist2.printList()

result_head = llist1.MergeTwoSortedLinkedLists(llist1.head, llist2.head)
print "Sorted Merge of two given LinkedLists : ",
while result_head:
	print result_head.val,
	result_head = result_head.next