dfclass Solution(object):
    def removeElements(self, head, val):
    	if head is None:
            return None
        current = head
        last = None
        while current is not None:
            if current.val == val:
                if last is not None:
                    last.next = current.next
                else:
                    head = current.next
                    last = None
            else:
                last = current
            current = current.next
        return head

"""
Remove all elements from a linked list of integers that have value val.
Example
Given: 6 --> 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

current = 6, last = None, head = 1, current = 1
current = 1, last = 1, current = 2
current = 2, last = 2, current = 6
current = 6, last.next = 3, current = 3
current = 3, last = 3, current = 4
current = 4, last = 4, current = 5
current = 5, last = 5, current = 6
current = 6, last.next = None, current = None

"""