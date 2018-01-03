# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-03 19:12:45
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-01-03 19:43:45
# Remove Nth from End of a LinkedList
# If N is greater than the length of the linkedlist, then remove the first node of LL
class ListNode:
	def __init__(self, data):
		self.val = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	# Function to reverse the linkedlist
	def RemoveNthNodefromEnd(self, head, N):
		if head is None or N <= 0:
			return head
		# use two pointers, slow and fast
		slow = fast = head
		count = 0
		# traverse the LL N times
		while(fast and count < N):
			fast = fast.next
			count += 1

		# fast becomes None when N > length of LL
		if(fast == None):
			# remove head node
			temp = head
			if(head):
				head = head.next
			temp = None
			return head

		prev_of_slow = None
		while(slow and fast):
			prev_of_slow = slow
			slow = slow.next
			fast = fast.next

		prev_of_slow.next = slow.next
		slow = None
		return head
		
	# insert a new element at the beginning of a list
	def push(self, new_data):
		new_node = ListNode(new_data)
		new_node.next = self.head
		self.head = new_node

	# prints the contents of a list
	def printList(self, head):
		temp = head
		while(temp):
			print temp.val,
			temp = temp.next

# create a linked list with user input
llist = LinkedList()
len = input("Enter the number of elements in LinkedList : ")
print "Enter elements : "
for i in range(0, len):
	llist.push(input())

N = input("Enter the value of N : ")
print "LinkedList before Removing Nth Node from end : ", llist.printList(llist.head)
llist.head = llist.RemoveNthNodefromEnd(llist.head, N)
print "LinkedList after Removing Nth Node from End : ", llist.printList(llist.head)