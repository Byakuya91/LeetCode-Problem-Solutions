class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # STEP ONE: sort the array and get the sum of the first three elements of the Array
        nums.sort()
        
        res = sum(nums[:3])
        
        # STEP TWO: loop through the array
        
        for i in range(len(nums)-2):
            # STEP THREE: create the pointers
            l = i + 1
            r = len(nums)-1
            
            # STEP FOUR: while loop on the pointers.
            while l < r:
                currSum = nums[i] + nums[l] + nums[r]
                
                # STEP FIVE: checking the currSum with the result
                if abs(currSum-target) < abs(res-target):
                    # Update the res
                    res = currSum
                    
                if currSum < target:
                    # Update the pointer
                    l+=1
                else:
                    r-=1
                    
        return res
                    
        
        
        
        
        '''
        PLAN OF ATTACK
        1) understand the problem(DONE)
        
        2) Psuedo Code the solution
            I want to sort the Array.
            I want to then loop through the array(using range) with left and right pointers.
            I want to create a result where I sum up the first three values
            I want to compare the absolute value of  sums of the left and right pointers and i to the absolute value of the result sum.
            If the sum is LESS than the resulting sum, then the result sum will be updated.
            
            If the sum is GREATER than the target, we increment the left pointer.
            
            If the sum is LESS than target, we shall decrement the right pointer
            
            After which we can return the result 
        '''
        