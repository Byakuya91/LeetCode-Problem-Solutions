class Solution(object):
    def longestCommonPrefix(self, strs):
        
        """
        :type strs: List[str]
        :rtype: str
        """
        #POA(Plan of Attack )
        #1) find the shortest string length and create a base case 
        #2) we will take the first string and match each character one by one 
        # 3) If there is a character that does NOT match,  the loop will break
        
        # longest_common_prefix variable 
        longest_common_prefix = ""
        
        
        # Base condition 
        if strs is None or len(strs) == 0:
            return longest_common_prefix
        
        # find the minimum length string from the array
        minimum_length = len(strs[0])
        
        for i in range(1, len(strs)):
            minimum_length = min(minimum_length, len(strs[i]))
            
        # Loop until the minimum_length
        for i in range(0,minimum_length):
            # grab the current character from the first string
            current_char = strs[0][i]
            
            # Check to see if this current character is found in all the strings or not
            for j in range(0, len(strs)):
                if strs[j][i] != current_char:
                    return longest_common_prefix
                
            longest_common_prefix+= current_char
            
        return longest_common_prefix
            
            
        
     
         
            
       
            
        
         
            
            
        
        
                 
        