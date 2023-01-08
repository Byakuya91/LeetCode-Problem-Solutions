class Solution(object):
    def intToRoman(self, num):
        
         # POA 
         # 1) Figure out what the problem is(DONE)
         # 2) Create a method  holding the values and all edge cases(DONE)
        # 3) Create a  loop that performs mod and int division on numbers and assigns symbols if it checks out.
       
          # STEP ONE: create a list of nested lists, holding all the symbols and edge cases.
          # It's a lst because checks will be done in an order from largest to smallest
             
        symbol_lst = [["I",1], ["IV",4], ["V",5],  
                  ["IX",9], ["X",10],["XL",40], 
                  ["L",50], ["XC",90],["C",100], 
                  ["CD",400], ["D",500],["CM",900], 
                  ["M",1000]]
        
        # STEP TWO: create a result to hold the symbols
        result = ""
        
        # STEP THREE: create a loop, iterating through the reversed list. This will use tuple unpacking.
        for sym, val in reversed(symbol_lst):
            # checking if the num and val do not equal zero
            if num // val:
                # store count for symbols calculated
                count = num // val
                # update the result. Remember, symbols are strings and strings * int returns copies.
                result+= (sym * count)
                # update the number for next iteration
                num = num % val
        return result
        
        
    
            
    
    