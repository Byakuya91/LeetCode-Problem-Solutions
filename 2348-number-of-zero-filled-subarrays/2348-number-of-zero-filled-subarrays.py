class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        
       # STEP ONE: create a pointer and a result variable
        i, res = 0,0
        
       # looping while the pointer is in bounds
        
        while i < len(nums):
            zero_Count = 0
            
            while i < len(nums) and nums[i] == 0 :
                # updating counter and shifting the pointer
                zero_Count+=1
                i+=1
                # adding zero_Count to result
                res+=zero_Count
            
            # updating pointer even if a zero does NOT exist
            i+=1
            
        return res