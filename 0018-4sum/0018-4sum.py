class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
          
        '''
        PLAN OF ATTACK(POA)
        1) Understand the problem(DONE)
        
        
        2) Notes and Psudo Code(DONE)
           You do NOT want duplicates
           You can do this by incrementing a pointer so that way it ends at a new value.
           You can elminate the duplicates by SORTING the array.
           Duplicates will be NEXT to one another
           When calculating the values we want to DECREMENT the right pointer
           If you INCREMENT the left pointer, the value is going to be larger(Remember, the array will be SORTED)
           
            You  can have the solution be N^3 space time complexity with nested for and while loops, but you want a GENERIC solution.
            The reason being is that if the k value of sums is 5,6,7; coding those loops wiill be harder.
            The solution is to implement RECURSION.
            
           
        
        '''
        
        
        # STEP ONE: SORT the array
        nums.sort()
        
        # STEP TWO declare key variables for the result and quadrupulets
        res,quad = [],[]
        
        # STEP THREE: create a function for the recursion
        def kSum(k,start,target):
            # Establish the none base case
            if k !=2:
                # For loop being inclusive so as there are at least some values left to form the Quad
                for i in range(start, len(nums)-k+1):
                    # taking into account of duplicates
                    if i > start and  nums[i] == nums[i-1]:
                        continue 
                    
                    quad.append(nums[i])
                    kSum(k-1, i+1, target - nums[i])
                    quad.pop()
                return
            
            # BASE CASE
            l,r = start, len(nums)-1
            
            while l < r:
                if nums[l] + nums[r] < target:
                    l+=1
                    
                    
                elif nums[l] + nums[r] > target:
                    r-=1
                    
                
                else:
                    res.append(quad + [nums[l], nums[r]])
                    # UPDATE the pointers to avoid an infinite Loop
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
        kSum(4,0,target)
        return res
          
                
        
        
        
      
        