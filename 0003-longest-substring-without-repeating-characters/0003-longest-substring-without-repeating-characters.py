class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # PLAN OF ATTACK
        # 1) One method is brute forcing, checking every substring if it has any duplicates
        # if it doesn't, we return the length
        #The problem with this method is that it will take forever to compute given the 
        # algorithm is checking every substring from the first char
        #2) proposed solution: sliding window technique
        #This is done by checking substrings for duplicate characters and popping off the leftmost char and reducing the window
        # The result should calculate the longest substring without duplicate characters once done
        # 3) code wise this is represented with a set to which characters are removed and add to the set 
        # with the aid of a left and right pointer.
       
        
        
        # STEP ONE:define a set of characters
        charSet = set()
        
        # STEP TWO:define a left pointer, and a result to hold the substring length
        l = 0
        sub_S_res = 0
        
        # STEP THREE: loop through the list
        for r in range(len(s)):
            
            # STEP FOUR: update the charSet
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            # adding a char to the set if isn't inside the set
            charSet.add(s[r])
            # updating the result
            sub_S_res = max(sub_S_res, r - l + 1)
            
         #STEP FIVE return the result    
        return sub_S_res
            
       
         
        
      