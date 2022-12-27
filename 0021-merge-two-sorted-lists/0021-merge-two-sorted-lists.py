# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #POA(PLAN OF ATTACK)
        # 1) Check to see if the lists are empty.
        # 2) determine the head of the resultant list. The head has to be smaller than the head of the given lists.
        #3) Loop through each node of the lists until one of the lists get traversed completely.
        # 4) While traversing the lists, identify smaller of the nodes of the lists and add it to the resultant list.
        #5) When the loop is complete, there will be a case where a list has nodes remaining. Add those remaining nodes to the resultant list.
        
       # BEFORE STEPS: simply the list names
        
        L1 = list1
        L2 = list2
        
       # STEP ONE: Check if either of the lists is null
        if L1 is None:
            return L2
        if L2 is None:
            return L1
        
        
       # STEP TWO: choose the head of the smaller of the two lists.
        if L1.val < L2.val:
            temp = head = ListNode(L1.val)
            L1 = L1.next
        else:
            temp = head = ListNode(L2.val)
            L2 = L2.next
            
      # STEP THREE:Loop until any of the lists become Null
     
        while L1 is not None and L2 is not None:
            if L1.val < L2.val:
                temp.next = ListNode(L1.val)
                L1 = L1.next
            else:
                temp.next = ListNode(L2.val)
                L2 = L2.next
                
            temp = temp.next
            
    # STEP FOUR:    Add all the nodes in L1, if remaining
    
        while L1 is not None:
            temp.next = ListNode(L1.val)
            L1 = L1.next
            temp = temp.next
            
   # STEP FIVE:    Add all the nodes in L2, if remaining
       
        while L2 is not None:
            temp.next = ListNode(L2.val)
            L2 = L2.next
            temp = temp.next
            
        return head 

        
            
            
                
            
         
         
        
            
                
                
        
         
        
        
        
        
    
    
        