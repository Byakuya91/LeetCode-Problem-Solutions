class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        # PLAN OF ATTACK
        # 1) Understand the problem(DONE)
        # 2) Understand what a Palindrone is(DONE)
         # 3) Code up a solution for odd and even length Palindrone substrings        
      
        
        # STEP ONE: intialize the result and its length
        result = ""
        
        resLen = 0
        
        
        # STEP TWO: Loop through every single POSITION in the string
        for i in range(len(s)):
            #Odd length palindrones
            l,r = i,i
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                     #Update the result(we know it's a Palindrone)
                    result = s[l:r+1]
                    
                    resLen = r-l+1
                    
                    
                # Update the pointers
                l-=1
                r+=1
             
            l,r = i, i+1
             # even length palindrones    
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    result = s[l:r+1]
                    
                    resLen =  r-l+1
                    
                l-=1
                r+=1
                    
                
          
                
        return result 
                    
                    
                    
                    
            
                
                
                
        
        
        