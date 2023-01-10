class Solution(object):
    def maxSubArray(self, nums):
        
        #POA(PLAN OF ATTACK)
        # 1) Understand the problem
        # 2) A cubic solution but the most inefficient solution
        # 3) Linear solution is better
        # 4) LS includes utilizing Kadane's algorithm to remove any negative number that prefixes the sequence.
        # 5) The process is akin to a sliding window where one is sliding the pointer and omitting negative nums due to them not contributing to the sum.
        
        # STEP ONE intialize a MaxSubArray 
        maxSubArr = nums[0]
        # STEP TWO intialize the current sum
        curSum = 0
        
        # STEP THREE: loop through each number
        for num in nums:
            # check for a negative prefix inside array.
            if curSum < 0:
                # reset the Sum back to zero.
                curSum =0
            # update the curSum
            curSum+=num
            # update the maxSubArr
            maxSubArr = max(maxSubArr, curSum)
        # return the maxSubArr        
        return maxSubArr
                
            