class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head is None: return None

        head_copy = head
        temp = None
        counter = 0

        while head is not None:
            head = head.next
            if counter == n:
                temp = head_copy
            if counter > n:
                temp = temp.next
                
            counter += 1
            

        if temp is None:
            return head_copy.next
        else:
            temp.next = temp.next.next

        return head_copy


"""        
Maintain two pointers – reference pointer and main pointer. 
Initialize both reference and main pointers to head. 
First move reference pointer to n nodes from head. 
Now move both pointers one by one until reference pointer 
reaches end. Now main pointer will point to nth node 
from the end. Return main pointer.


1 2 3 4 

head_copy = 1
i = 1, head = 2
i = 2, temp = 1, head = 3
i = 3, temp = 2, head = 4
i = 4, temp = 3, head = 5
i = 5, break

3-> 5

return head_copy
"""