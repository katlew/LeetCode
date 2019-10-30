"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

// 2 4 3
// 5 6 4
// 7 0 8
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ListNode(0)
        currentNode = res
        x = l1
        y = l2
        carry = 0

        while x or y:
            a = x.val if not x is None else 0
            b = y.val if not y is None else 0

            sum = carry + a + b
            carry = math.floor(sum / 10)
            currentNode.next = ListNode(sum % 10)
            currentNode = currentNode.next

            if x is not None:
                x = x.next
            if y is not None:
                y = y.next
        
        if (carry == 1):
            currentNode.next = ListNode(1)
        return res.next


"""
Complexity Analysis:

Time Complexity : O(max(m, n)).
Assume that m and n represents the length of l1 and l2 respectively,
the algorithm above iterates at most max(m, n) times.

Space complexity: O(max(m,n)).
The length of the new list is at most max(m,n) + 1.
"""