class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
           
        """
        Plan of Attack
        1) Understand the problem
        2) Compile a solution
        3) One solution is iterate left and right, check for target and return index of target.
        4) The result should be O(n) complexity.
        5) The array is sorted and that can be utilized to where it is Log n
        6) Binary Search utilizes a left and right pointer index zero and end of the list
        7) We can comput the averages of the left and right pointer to get the index
        8) We can increment the left pointer and check for the target and if found, return the Index.
        9) BIG question: What if we do NOT find the target.
        10) Instead of shifting the pointer to the LEFT we can shift it to the RIGHT.
        11) Check if the target exists if it does not exist, we return the Index where it would exist.
        
        
        
        """
        
        
        
        # STEP ONE: intialize left and right pointers
        l,r = 0, len(nums)-1
        
        # STEP TWO: execute Binary search with a While Loop
        
        while l<= r:
            # create the middle pointer
            mid = (l+r)//2
            
            # Check if we FOUND the target
            if target == nums[mid]:
                return mid
            
            # If the target is GREATER than the mid value
            if target > nums[mid]:
                # Search to the right by updating LEFT pointer
                l = mid + 1
                
            # If the target is LESS than the mid value 
            else:
                # Searc to the left by updating the RIGHT pointer.
                r = mid -1 
                
                
        # If NO target is found. The reason why LEFT pointer works is because even if pointer goes out of bound, it will return index of the position where the target WOULD have been located. So if we have an array of [2] and target = 1. 
        #  The LEFT and RIGHT pointers would check and see that one is LESS than TWO and the RIGHT pointer shifts and is OUT OF BOUNDS.
        # From there, the index of zero is returned because it inserts the target =1  into array of [2] to equal  [1,2]
        return l 
                
                
        
        
  
            
        
     
        
        