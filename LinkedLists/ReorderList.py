# -*- coding: utf-8 -*-
# @Author: Manju S V
# @Date:   2018-04-21 17:20:12
# @Last Modified by:   Manju S V
# @Last Modified time: 2018-04-21 18:06:29

# Given a singly linked list

#     L: L0 → L1 → … → Ln-1 → Ln,

# reorder it to:

#     L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …


class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # @param head : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, head):
        count = 0

        if head is None or head.next is None or head.next.next is None:
            return head

        temp, cur = head, head
        prev, prev1, fut, fut1, fut2 = None, None, None, None, None
        # count No of Nodes
        while temp:
            count = count + 1
            temp = temp.next

        # traverse till middle of linked list
        for i in range(0, count / 2):
            prev = cur
            cur = cur.next

        prev.next = None

        # reverse the second half of the linked list
        while cur:
            fut = cur.next
            cur.next = prev1
            prev1 = cur
            cur = fut

        cur1 = head

        # Now attach each node of first list with each node of second list
        while cur1 and prev1:
            fut1 = cur1.next
            fut2 = prev1.next
            cur1.next = prev1
            if fut1:
                prev1.next = fut1
            cur1 = fut1
            prev1 = fut2

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

result_head = llist.reorderList(llist.head)
print "LinkedList after reordering : ", llist.printList(result_head)
