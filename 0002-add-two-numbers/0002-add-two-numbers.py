# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # NEW POA
        
        # STEP ONE: create a dummy node to handle edge cases
        dummy = ListNode()
        # curr is pointing at a new postion that the digit will be inserted into
        cur = dummy
        
        # STEP TWO: iterate through the nodes of the LinkedList
        # Keeps tracks of carry values whenever the val of LinkedList are added
        carry_val = 0
        while l1 or l2 or carry_val:
            # grabbing the value from the LinkedList, other wise it is 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # STEP THREE: computing the new digit
            val = v1 + v2 + carry_val
            # remove the carry from summed digit
            carry_val = val //10
            # accounting for carry greater than ten
            val = val % 10
            
            # inserting sum into LL
            cur.next = ListNode(val)
            
            # STEP FOUR: update the pointers!
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next
            
            
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            