# Given the head of a singly linked list, group all the nodes with odd indices together 
# followed by the nodes with even indices, and return the reordered list.
# The first node is considered odd, and the second node is even, and so on.
# Note that the relative order inside both the even and odd groups should remain as it was in the input.
# Ex: input: 1->2->3->4->5  output: 1->3>->5->2->4

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None or head.next.next is None:
            return head
        lastNode = head
        nrofNodes = 0
        while(lastNode.next):
            nrofNodes += 1
            lastNode = lastNode.next
        
        cur = head
        even = False
        prev = None
        count = 0
        while(cur and count < nrofNodes+1):
            if even:
                prev.next = cur.next
                cur.next = None
                lastNode.next = cur
                lastNode = lastNode.next
                cur = prev.next
                even = False
            else:
                prev = cur
                cur = cur.next
                even = True
            count += 1
        return head
    
    # insert a new element at the beginning of a list
    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.head
        self.head = new_node

    # prints the contents of a list
    def printList(self, head):
        res = []
        temp = head
        while(temp):
            res.append(temp.val)
            temp = temp.next
        return res
    
llist = LinkedList()
n = int(input("Enter the number of elements in LinkedList : "))
print("Enter elements : ")
for i in range(0, n):
    llist.push(int(input()))

print(f"head: {llist.head.val}")
print(f"Input LinkedList : {llist.printList(llist.head)}")

print(f"odd even LinkedList : {llist.printList(llist.oddEvenList(llist.head))}")
