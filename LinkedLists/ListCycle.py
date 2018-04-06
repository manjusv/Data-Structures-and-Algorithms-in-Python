# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-03 20:17:01
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-04-06 18:20:45

# Given a linked list, return the node where the cycle begins. If there is no cycle, return null


class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Function to find first Node in the cycle
    def FindFirstNodeCycle(self, head, slow):
        while(head and slow):
            if(head == slow):
                return slow
            head = head.next
            slow = slow.next

    # Function to reverse the linkedlist
    def Cycle(self, head):
        # use two pointers
        slow = fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            # check if two pointers intersect
            if(slow == fast):
                # there is a cycle, find starting node of cycle
                return self.FindFirstNodeCycle(head, slow)
        return None

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

print "Input LinkedList : ", llist.printList(llist.head)

# create a cycle
llist.head.next.next.next = llist.head.next

print "Staring Node val of cycle : "
if llist.Cycle(llist.head) is not None:
    print llist.Cycle(llist.head).val
else:
    print None
