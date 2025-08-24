# Problem: Reverse Linked List
# Link: https://leetcode.com/problems/reverse-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

# Example usage
if __name__ == "__main__":
    a = ListNode(1, ListNode(2, ListNode(3)))
    rev = reverseList(a)
    while rev:
        print(rev.val, end=" ")  # 3 2 1
        rev = rev.next
