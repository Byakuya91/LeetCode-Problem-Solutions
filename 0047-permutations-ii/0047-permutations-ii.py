class Solution(object):
    def permuteUnique(self, nums):
        
        #PLAN OF ATTACK(POA)
        # 1) Understand the problem
        # 2) Refresh yourself on permutations 
        #  2A) a permutation is the mathematical way a set of numbers can be arranged. This is represented with
        # factorial. n! n being the number of elements inside a list or set so 3! = 3 * 2 * 1 or 6 total combinations. 
        # HOWEVER it is NOT six here because we CANNOT use duplicates. So if a list of [1,1,2] equals [1,1,2], [1,2,1] etc. 
        # Notice how we cannot reuse values. So in this case because this list has two ones we can't swap one for the 
        # for the one. 
        # This can be showcased through a decision tree. 
        # One method is modifying a list and using a Hashmap to solve the problem and backtrack
        # update the counts for each value used to avoid having  duplicates. 
        # You can increment or decrement the counts
        
        # STEP ONE: create a variable to store the permutation list results and permutations values.
        
        perm_Lst_res = []
        
        perm = []
        
        # Create a count dictionary with an intial count of zero
        perm_Count = {n:0  for n in nums}
        
        # STEP TWO: update the counts for the Hashmap with all the values in the Perm list
        for n in nums:
            perm_Count[n]+=1
            
        # STEP THREE: create a function for Depth First Search required for the problem.
        # No parameters need to be passed because one can access these above variables due to it being nested in this function.
        
        def depth_first_search():
            # define a base case
            if len(perm) == len(nums):
                # The reason why copy is being employed is because there is only ONE perm and that will be
                # be updated.
                perm_Lst_res.append(perm[:])   # NOTE, you can also use list function or slice it to copy it. 
                return 
            
            # Brute Force method: go through every value in perm_Count. Remember, perm_Count has elminated duplicates with keys and values.
            for n in perm_Count:
                # checking if we can choose a count for a permutation
                if perm_Count[n] > 0:
                    # add the value to Perm.
                    perm.append(n)
                    
                    # update the count
                    perm_Count[n]-=1
                    
                    # Recursively call depth_first_search
                    depth_first_search()
                    
                    # STEP FOUR: clean up step
                    
                    # add to the Count
                    perm_Count[n]+=1
                    
                    # remove the value we just added to perm
                    perm.pop()
         
        
        # STEP FIVE: call depth_first_search and return the result
        depth_first_search()
        
        return perm_Lst_res
                    
                    
            
            
            
            
        
        
        
        
        
        
       
        