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
        reversed_list = None
        current = head

        while current is not None:
        	# store next node
        	next_node = current.next
        	if reversed_list is None:
        		reversed_list = current
        		reversed_list.next = None

        	# insert into head of reversed_list
        	else:
        		current.next = reversed_list
        		reversed_list = current

        	current = next_node
        return reversed_list