# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-03 17:35:10
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-01-03 18:40:22

# given a LinkedList, check if it is a Palindrome or not
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

	# Function to reverse the LinkedList
	def ReverseList(self, head):
		cur = head
		prev = None
		while(cur):
			fut = cur.next
			cur.next = prev
			prev = cur
			cur = fut
		return prev

	# Function to reverse the linkedlist
	def isPalindrome(self, head):
		# if head is None return True
		if head == None:
			return True
		# use two pointers, slow and fast
		slow = head
		fast = head
		prev_of_slow = None

		while(fast and fast.next):
			prev_of_slow = slow
			slow = slow.next
			fast = fast.next.next

		if(fast == None):
			# The LL is even
			prev_of_slow.next = None
		else:
			if(prev_of_slow and prev_of_slow.next):
				prev_of_slow.next = None
			mid = slow
			slow = slow.next

		# divide the list into first half and second half
		first = head
		second = self.ReverseList(slow)

		# Now check for palindrome
		while(first and second):
			if(first.val != second.val):
				return False
			first = first.next
			second = second.next
		# return true when all elements match
		return True

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
llist = LinkedList()
n = input("Enter the number of elements in LinkedList : ")
print "Enter elements : "
for i in range(0, n):
	llist.push(input())

print "Input LinkedList  : ", llist.printList()
if llist.isPalindrome(llist.head):
	print "The LinkedList is Palindrome"
else:
	print "The LinkedList is not a palindrome"