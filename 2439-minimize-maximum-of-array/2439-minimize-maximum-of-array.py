class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        # STEP ONE: create a result variable and set it equal to the total 
        res = total=  nums[0]
        
        # STEP TWO: iterate through the array. We're skipping the first value because we can't move the values
        # to the left. 
        for i in range(1, len(nums)):
            # update the total and res
            total+=nums[i]
            res = max(res, math.ceil(total/ (i+1)))
            
        return res
            
            
        
        
        
        
        # UNDERSTANDING THE PROBLEM(DONE)
        # CODE UP A SOLUTION(ONGOING)
        
        