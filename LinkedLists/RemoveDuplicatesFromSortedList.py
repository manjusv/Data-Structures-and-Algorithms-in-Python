# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2019-07-09 10:50:03
# @Last Modified by:   Manju S V
# @Last Modified time: 2019-07-09 11:17:07

# given a sorted LinkedList, remove duplicate nodes from it


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head

        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head

    # insert a new element at the beginning of a list
    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    # prints the contents of a list
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.val, end="-->")
            temp = temp.next


# create a linked list with user input
llist = LinkedList()
n = int(input("Enter the number of elements in LinkedList : "))
print("Enter elements : ")
for i in range(0, n):
    llist.push(input())

print("Input LinkedList  : ")
llist.printList()
llist.deleteDuplicates(llist.head)
print("\nLinkedList after deleting duplicates : ")
llist.printList()
