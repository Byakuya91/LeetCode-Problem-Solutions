class Solution(object):
    def removeDuplicates(self, nums):
        # STEP ONE intialize pointers
        l = 1
        
        
        # STEP TWO iterate through the list
        
        for r in range(1,len(nums)):
            # check if the value is an existing value in list OR a new value in the list
            if nums[r] != nums[r-1]:
                # take the unique value and place it at index L
                nums[l] = nums[r]
                # increment the left pointer. NOTE we don't need to increment the r pointer because the for Loop is incrementing it. 
                l+=1
            r+=1
        return l
        
        
        """
       PLAN OF ATTACK
       1) Understand the problem
       2) Draw it out
       3) implement a solution
        """
        