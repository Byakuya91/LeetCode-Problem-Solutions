class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # SECOND SOLUTION
        
        # STEP ONE: define counter and result variables
        zero_Count,res = 0,0
        
        # STEP TWO: for loop through the list of numbers
        for i in range(len(nums)):
            # if the value is zero
            if nums[i] == 0:
                # increment the count
                zero_Count+=1
            else:
                # reset count
                zero_Count = 0
            # STEP THREE: add the count to the result
            res +=zero_Count
            
        return res
                
        
        
        
        
        
        
        
        # FIRST SOLUTION
        
#        # STEP ONE: create a pointer and a result variable
#         i, res = 0,0
        
#        # looping while the pointer is in bounds
        
#         while i < len(nums):
#             zero_Count = 0
            
#             while i < len(nums) and nums[i] == 0 :
#                 # updating counter and shifting the pointer
#                 zero_Count+=1
#                 i+=1
#                 # adding zero_Count to result
#                 res+=zero_Count
            
#             # updating pointer even if a zero does NOT exist
#             i+=1
            
#         return res