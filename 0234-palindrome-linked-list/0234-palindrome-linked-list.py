# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        # OPTIMAL solution
        
        # create a fast and slow pointer for LinkedList
        fast_ptr = head
        slow_ptr = head
        
        # shifting the pointers to find the middle(slow pointer)
        while fast_ptr and fast_ptr.next:
            
            # update fast ptr
            fast_ptr = fast_ptr.next.next
            # update slow pointer
            slow_ptr = slow_ptr.next
            
        # reverse second half of LinkedList  
        prev_node = None  
        
        while slow_ptr:
            tmp = slow_ptr.next
            slow_ptr.next = prev_node
            prev_node = slow_ptr
            slow_ptr = tmp
            
        # check if LinkedList is a Palindrone
        left_ptr, right_ptr = head, prev_node
        
        while right_ptr:
            # comparing pointers
            if left_ptr.val != right_ptr.val:
                return False
            left_ptr = left_ptr.next
            right_ptr = right_ptr.next 
            
       # If we have a palindrone 
        return True 
        
        
        
        
        
        # POA
        # 1) Understand what a Palindrone is(DONE)
        # 2) Implement a solution using an Array
        # 3) If successful with two, implement a more optimal solution.
        
        
        # STEP ONE create an array:
        # nums = []
        
        # Append each LinkedList value into our array
        # while head:
        #     nums.append(head.val)
        #     head = head.next
        
        # Solve for Palindrone
#         left_pointer, right_pointer = 0, len(nums)-1
        
        # while left_pointer <= right_pointer:
            # if there is no palindrone in the list
#             if nums[left_pointer] != nums[right_pointer]:
#                 return False
            
#             left_pointer+=1
#             right_pointer-=1
        
#         return True 
        
        
        
        
        