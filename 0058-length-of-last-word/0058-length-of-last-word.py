class Solution:
    def lengthOfLastWord(self, s: str) -> int:
          
        """
        PLAN OF ATTACK
        1) Understand the problem
        2) Come up with a solution
        3) Implement a solution
        
        
        
        """
        
        # STEP ONE: intialize pointers
        i, length = len(s) -1, 0
        
        # STEP TWO Elminate the white space
        while s[i] == " ":
            i-=1 # REMEMBER, we are starting from the end of the string. 
            
       # STEP THREE: counting the characters
        while i >=0 and s[i] != " ":
            # increment the length
            length+=1
            # update the i pointer
            i-=1
        # STEP FOUR: return the length
        return length 
            
        
        
      
       
   