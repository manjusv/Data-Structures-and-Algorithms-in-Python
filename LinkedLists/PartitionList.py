# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-04-22 13:41:23
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-04-23 00:02:05


class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # @param head : head node of linked list
    # @param x : integer
    # @return the head node in the linked list
    def partition(self, head, x):
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        dummy1 = ListNode(0)
        temp1 = dummy1
        while head:
            if head.val < x:
                temp = temp.next
            else:
                temp.next = head.next
                temp1.next = head
                temp1 = temp1.next
            head = head.next
        temp1.next = None
        temp.next = dummy1.next
        return dummy.next

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
n = input("Enter the number of elements in LinkedList : ")
print "Enter elements : "
for i in range(0, n):
    llist.push(input())

print "Input LinkedList : ", llist.printList(llist.head)

x = input("Enter value of x : ")

result_head = llist.partition(llist.head, x)
print "LinkedList after Partitioning : ", llist.printList(result_head)
