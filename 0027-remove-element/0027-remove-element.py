class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        
        # STEP ONE: intialize the pointer
        k = 0
        
        
        # STEP TWO: iterate through every value of the array
        
        for i in range(len(nums)):
            # if the nums isn't equal to Val, we don't perform the swap
            if nums[i] != val:
                # This should be similar to quick-sort where we parition
                nums[k] = nums[i]
                # Update the pointer
                k+=1
                
        # return the number of elements that do NOT have the value
        return k
        
        
        """
        POA(Plan of Attack)
        1) Understand the problem(DONE)
        2) Understand how pointers work and draw it out(DONE)
        3) implement the solution(DONE)
        
        """
        