class Solution(object):
    def lengthOfLIS(self, nums):
         #PLAN OF ATTACK(POA)
        # 1) Understand the problem(DONE)
        # 2) One possible approach is brute force with Depth first Search
        # We can traverse the array and choose whether or not to include the value or remove it.
        # Mathematically this equates to 2**n  Where 2 equals the number of combinations and n is input array size.
        # This however will create a situation where N**2 complexity is there and it isn't efficent, but we can mod it
        # to be a lot more efficient: Depth First Search with Cache
        # Elminating extra work by starting at the last index and figuring out the total number of combinations to make 
        # a longest increasing subsequence. 
        # We can also accomplish this with DYNAMIC programming as well.
        # 3) DYNAMIC programming solution
        # Start at the last value in the list and work backwards
        # You can take the MAX of value starting at a position, comparing it to the left or right and from there
        # you can construct the Longest Increasing Subsequence(LIS)
        # Note the space, time complexity should be  O = N**2 because we are starting backwards.
        
        # STEP ONE: establish a cache or list
        # LIS = Longest Increasing Subsequence
        LIS =  [1] * len(nums)
        
        # STEP TWO: iterate through every index of the input array
        
        # NOTE: we are starting backwards and moving backwards
        for i in range(len(nums)-1,-1,-1):
            # Iterate through every subsequence that comes after i
            for j in range(i+1, len(nums)):
                # checking if the value at i is LESS than the value at j
                if nums[i] < nums[j]:
                    # Updating LIS at i
                    LIS[i] = max(LIS[i], 1 + LIS[j])
                    
        # return the LIS for the greatest value will equal the len of LIS
        return max(LIS)
        
        
        
        
       
        
        
        