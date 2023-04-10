class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # PLAN OF ATTACK
        #1) Sort the potions and then Binary search
        
        # STEP ONE: sort the potions and create a result
        n = len(spells)
        
        m = len(potions)
        
        pairs = [0] * n
        
        potions.sort()
        
        for i in range(n):
            
            spell = spells[i]
            
            left = 0
            
            right = m - 1
            
            while left <= right:
                
                mid = left + (right - left) // 2
                
                product = spell * potions[mid]
                
                if product >= success:
                    
                    right = mid - 1
                    
                else:
                    left = mid + 1
                    
            pairs[i] = m - left
            
        return pairs

        
# OLD CODE

# # PLAN OF ATTACK
#         #1) Sort the potions and then Binary search
        
#         # STEP ONE: sort the potions and create a result
#         potions.sort()
#         result = []
        
#         # STEP TWO: go through the spells array and execute binary search
#         for s in spells:
#             # binary search
            
#             #1) Declare left and right pointers
#             l,r = 0, len(spells)-1
            
#             idx = len(potions)  # find the (furthest to the LEFT)weakest potion that WORKS
            
#             #2) When the pointers don't cross
#             while l <=r:
#                 m = (l+r)//2
#                  # conditions to check if the potions are a success.
#                 if s * potions[m] >= success:
#                     r = m-1
#                     idx = m
                    
#                 else:
#                     l= m+1
#             result.append(len(potions)-idx)      
                    
            
            
#         return result 
            
            
        
        
        