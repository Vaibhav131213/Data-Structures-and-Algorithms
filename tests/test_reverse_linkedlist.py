import unittest
from Python.LinkedList.reverse_linkedlist import ListNode, reverseList

class TestReverseLinkedList(unittest.TestCase):
    def list_to_array(self, head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    def test_examples(self):
        a = ListNode(1, ListNode(2, ListNode(3)))
        rev = reverseList(a)
        self.assertEqual(self.list_to_array(rev), [3,2,1])

        b = ListNode(1)
        rev = reverseList(b)
        self.assertEqual(self.list_to_array(rev), [1])

        self.assertIsNone(reverseList(None))

if __name__ == "__main__":
    unittest.main()
