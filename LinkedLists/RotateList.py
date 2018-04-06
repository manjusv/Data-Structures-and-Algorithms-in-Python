# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-01-07 18:04:50
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-04-06 18:26:59

# Given a list, rotate the list to the right by k places, where k is non-negative.
# Given 1->2->3->4->5->NULL and k = 2
# return 4->5->1->2->3->NULL.


class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, head, k):
        cur = head
        # count the number of nodes in LinkedList
        count = 0
        while(cur):
            count = count + 1
            cur = cur.next

        # if no of nodes in LL is same as k, no rotation needed
        if(count == k):
            return head
        else:
            k = k % count

        # if k is 0, then no rotation
        if(k == 0):
            return head

        # divide LL to two parts, one part contains last k nodes
        cur = head
        prev = None
        i = 1
        while(cur and i < (count - k + 1)):
            prev = cur
            cur = cur.next
            i = i + 1

        # set next of last node of first part to null
        prev.next = None

        temp = cur
        # traverse the second part till last node
        while(cur and cur.next):
            cur = cur.next

        # join last node of second part to head
        cur.next = head
        head = temp

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
n = input("Enter the number of elements in LinkedList : ")
print "Enter elements : "
for i in range(0, n):
    llist.push(input())

print "Input LinkedList : ", llist.printList(llist.head)

k = input("Enter value of k : ")

result_head = llist.rotateRight(llist.head, k)
print "LinkedList after rotating by k elements : ", llist.printList(result_head)
