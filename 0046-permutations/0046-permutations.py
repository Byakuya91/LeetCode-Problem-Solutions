class Solution(object):
    def permute(self, nums):
          # PLAN OF ATTACK(POA)
        # 1) Understand the problem(DONE)
        #2) Understand a permutation(DONE)
         #3) Utilize recursion and setup permutations 
          #4)  remove the first num on list
          #5)Do a recursive call on perms with the modified nums
           #6) Use extend to add perms to perms result and append popped value to perms(Remember, it will be called recursively and execute again)
            # 7) return the perm_result outside the nested for loops.  
        
        #STEP ONE: define the result with the number of permutations
        perm_result = []
        
        # STEP TWO: define a base case for recursion
        if (len(nums) == 1):
            return [nums[:]]
        
        # STEP THREE: iterate through every value of nums via for loop
        
        for i in range(len(nums)):
            
            # remove the first value from nums
            n = nums.pop(0)
            
            # create a recursive call(note we have one less num due to it being popped)
            perms = self.permute(nums)
            
            # STEP FOUR: iterate through remaining perms and add it to the result
            for perm in perms:
                # adding popped value back onto permutation
                perm.append(n)
            # add the permutations back to perm results
            perm_result.extend(perms)
            
            nums.append(n)
            
            
        return perm_result
          
        
        
     
        