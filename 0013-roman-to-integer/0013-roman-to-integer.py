class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # POA
        # Create a dictionary that holds all the values of the roman numerials
        # scan the string from left to right and grab the  value of the corresponding character
        # from the dictionary and add it to the result(FOR LOOP)
        # Account for a special case where the left current character has a value
        # LESS than the value of the corresponding character.
        # EX: if "X" = 10 and "IX" = 9 
        # In this case one needs to subtract the value of the char on the left from 
        # the result
        
        
        # create a dictionary that holds the values
        numerals_dic= {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        
        # get the length of the string
        # Strings will be "I" or "IV" so that needs to be taken into account
        
        numeral_len = len(s)

        # create a way to store the result
        
        # roman_nums = numerals_dic[numeral_len-1]
        roman_num = numerals_dic[s[numeral_len-1]]
        
        
        # loop through each character from LEFT to RIGHT
        for i in range(numeral_len-2,-1,-1):
            #Check if the character right of current char is bigger or smaller
            if numerals_dic[s[i]] >= numerals_dic[s[i+1]]:
                roman_num+=numerals_dic[s[i]]
            else:
                # subtract the value from the numeral and get the result
                roman_num-= numerals_dic[s[i]]
        return roman_num
            
              
                    
         
                    
                    
        
        
        
       