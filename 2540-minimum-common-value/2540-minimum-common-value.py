class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        # Define intersection of the sets of num1 and num2
        
        intersection = set(nums1) & set(nums2)
        
        # print(intersection)
        
        # NEW SOLUTION 
        return min(intersection or [-1])
        
        # create a conditional where if the intersection is true, return the minimum of it
        
        # OLD SOLUTION 
#         if intersection:
#             return min(intersection)
        
#         return -1 

       
         
        
            
        
        
        
        
        
        
      