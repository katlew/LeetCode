# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
        	return None

        stack = []
        current = head

        while current is not None:
        	stack.append(current)
        	current = current.next

        for i in xrange(len(stack)-1,0,-1):
        	stack[i].next = stack[i-1]
		
		stack[0].next = None
        return stack[-1] # last index 