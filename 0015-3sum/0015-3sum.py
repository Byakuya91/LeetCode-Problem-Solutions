class Solution(object):
    def threeSum(self, nums):  
      # POA
      # 1) Understand the problem. It's the same as two sum and two sum two.(DONE)
      # 2) Sort the list to avoid duplicates
      # 3) Utilize the pointer method of having a left and right pointer 
      # 4) Check if the two added elements of the list are greater or less than the sum
      # 5) the former, decrement the right pointer. The latter, increment the left pointer. 
      # 6) The pointers should NEVER cross and we are guaranteed a solution due to the numbers needing to add up.
      # 7) This will require nested loops and updating the pointers accordingly. 
    
        
        
        
        # STEP ONE: define the result. It's a list of lists and sort the nums.
        result = []
        nums.sort()
        
        # STEP TWO: use each number in the input array as the first value for computing the sum
        
        for i,a in enumerate(nums):
            # check to avoid using the same value for the first value of the list.
            if i > 0 and a == nums[i-1]:
                continue 
            # create two pointers for the solution
            l,r =  i+1,len(nums)-1
            # while loop to iterate through the rest of the lst and get a solution
            while l < r:
                # computing the sum
                three_Sum = a + nums[l] + nums[r]
                # checking if the sum is greater than zero
                if three_Sum > 0:
                    # decrease the right pointer
                    r-=1
                # checking for opposite condition
                elif three_Sum < 0:
                    # increase the left pointer
                    l+=1
                else:
                    # add numbers to result
                    result.append([a, nums[l], nums[r]])
                    # update the left pointer
                    l+=1
                    # while loop to check the left pointer has the same value
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return result
                        
                    
                    
                
            
                
        
        
    
      
      
      
        
        
        
        
        
    
        
        
        