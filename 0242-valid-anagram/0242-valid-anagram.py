class Solution(object):
    def isAnagram(self, s, t):
        # NEW SOLUTION(MORE OPTIMAL, Sorted)
        # The reason this works is because when the strings are sorted they should be equal due to the strings needing the same number of characters.
        # When both strings are sorted, the types of characters, As, Bs, Cs etc. should be the same and thus evaluate to true. 
        # the issue with this solution could be due to time complexity as some sorting algorithms, like bubble sort, will take longer. 
        return sorted(s) == sorted(t)
        
      # POA
      # 1) Understand the problem
      # 2) solution one: Hashmap solution
      # 3) figure out a more optimal solution
        
        
        # BRUTE FORCE SOLUTION(NOT OPTIMAL)
        
        # check if the strings are the same length
        # if len(s) != len(t):
        #     return False 
        
        # create a count for S and T
        # countS, countT = {},{}
        
        # iterate through s and t and populate the hashmaps of both.
        
#         for i in range(len(s)):
#             countS[s[i]] = 1 + countS.get(s[i],0)
#             countT[t[i]] = 1 + countT.get(t[i],0)
        # check if the HashMaps are the same.
            
#         for c in countS:
#             # if the counts are NOT the same.
#             if countS[c] != countT.get(c,0):
#                 return False
#         return True 
            
          # NEW solution
        
        
        
     