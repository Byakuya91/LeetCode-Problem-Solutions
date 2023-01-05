class Solution(object):
    def isValid(self, s):
         # Plan of Attack(POA)
         # 1) go through the string left to right
         # 2) if one encounters a left/opening parantheses, then push it to the stack data structure due to LIFO(Last in First Out)
         # 3) if one encounters a right/closing parantheses, check the top of the stack. If it is the correct corresponding open/left parenthesis, move              #   further, else  return false.
         # 4) At last, for valid string, the stack should be empty because all the left parentheses should have matched with the right ones.
        
        
           # a stack for left symbols
        leftSymbols = []
        
        # Loop through each character of the string input
        for char in s:
            # if the leftSymbol exists
            if char in  ['(', '{', '[']:
                leftSymbols.append(char)
                
             # if the right symbol is encountered
            elif char == ')' and len(leftSymbols) != 0 and leftSymbols[-1] == '(':
                leftSymbols.pop()
          
            elif char == '}' and len(leftSymbols) != 0 and leftSymbols[-1] == '{':
                leftSymbols.pop()
            elif char == ']' and len(leftSymbols) != 0 and leftSymbols[-1] == '[':
                leftSymbols.pop()
                
            # if none of the valid symbols are present
            else:
                return False
            
        return leftSymbols == []
            
        
        
        
        

       