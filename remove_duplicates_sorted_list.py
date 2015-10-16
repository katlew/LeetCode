# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
    	"""
    	: type head: ListNode
    	: rtype: ListNode
    	"""
    	if head is None:
    		return head
    	current = head

    	while current.next is not None:
    		if current.val == current.next.val:
    			temp = current.next
    			current.next = current.next.next
    			del temp

    		else:
    			current = current.next
    	return head