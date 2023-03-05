class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # STEP ONE: define left and right pointers.
        l,r = 0,0
        
        
        # STEP TWO: loop through the entire length of the array
        while r < len(nums):
            # STEP THREE: count how long the current streak of numbers in the array is
            count = 1 # whatever the pointer is at is going to be a new number.
            while r+1 < len(nums) and nums[r] == nums[r+1]:
                r+=1
                count+=1  
                
           # we want two values of the counted length and no more.
            for i in range(min(2,count)):
                # taking the right index value and swapping it with the left
                nums[l] = nums[r]
                # update pointers
                l+=1
                
            r+=1
        # This should get the total length of the list due to shifting the values into the index positions.   
        return l
        
        
        
        # 1) understand the problem(DONE)
        # 2) Code a solution
        
        
        