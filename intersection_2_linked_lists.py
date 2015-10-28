class Solution(object):
    def _length(self, head):
        current = head
        length  = 0
        
        while current != None:
            current = current.next
            length += 1
        
        return length

    def getIntersectionNode(self, headA, headB):
        lenA = self._length(headA)
        lenB = self._length(headB)
        
        # Make sure the list A is no longer that list B.
        if lenA > lenB:
            lenA, lenB   = lenB, lenA
            headA, headB = headB, headA
        
        # Handle with the special case.
        if lenA == 0 or lenB == 0:      return None
        
        # Skip the leading nodes in list B, which is impossible to be
        # the intersection node.
        currentA = headA
        currentB = headB
        for _ in xrange(lenB - lenA):
            currentB = currentB.next
        
        # Try to find the intersection node
        while currentA != None and id(currentA) != id(currentB):
            currentA = currentA.next
            currentB = currentB.next
        
        return currentA

"""
* Chris Hint : Look at the length
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3

* length headB = 6
* length headA = 5
* 6 - 5 = 1
* start headB (bigger one) at 1 over
* then compare each node in headA and headB

If the two linked lists have no intersection at all, return null.
Your code should preferably run in O(n) time and use only O(1) memory.

_ has 3 main conventional uses in Python:

To hold the result of the last executed statement in an interactive interpreter session. This precedent was set by the standard CPython interpreter, and other interpreters have followed suit
For translation lookup in i18n (imported from the corresponding C conventions, I believe)
As a general purpose "throwaway" variable name to indicate that part of a function result is being deliberately ignored
"""