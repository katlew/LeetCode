# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(-1)	# a pseudo head node
        current = head

        while l1 != None and l2 != None:
        	if l1.val <= l2.val:
        		current.next = l1
        		l1 = l1.next
        	else:
        		current.next = l2
        		l2 = l2.next
        if l1 != None:
        	current.next = l1	# extend remaining nodes
        else:
        	current.next = l2

        head = head.next	# remove pseudo head node
        
        return head