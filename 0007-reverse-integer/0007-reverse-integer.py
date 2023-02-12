class Solution:
    import math 
    def reverse(self, x: int) -> int:
        
        """
        PLAN OF ATTACK
        1) Understand the problem
        2) Create a solution
        3) keep in mind this is a 32 bit digit number. 
        4) 123 divided by mod ten can get rid of the 3 from the one's place.
        5)The result can then constructed by dividing by ten via integer division and the steps four and five are repeated.
        6) The result is then added as a reverse digit.
        7) BIG thing is to account for 64 bit digits and not having them factor in.
    
        """
        
        
        
        
        # STEP ONE: define a MAX and MIN integer for 32 bit and a variable to store result
        # Integer.MAX_VALUE = 2147483648(ends with 7)
        # Integer.MIN_VALUE = -2147483647(ends with -8)
        
        MAX = 2147483648
        
        MIN = -2147483647
        
        result = 0
        
        
        # STEP TWO: While loop to iterate
        while x:
            # create variable to hold the digits
            digit = int(math.fmod(x,10))   # Python can be dumb as normal mod division for Python -1 % 10 = 9
            x = int(x/10)                   # Python is also dumb with this as if done normally -1//10 = -1
            
            # Conditional statements to prevent the digits from overflowing.
            
            # If the MAX integer was too big for overflow OR the same as the MAX value moded by ten whhich is 7.
            if ((result > MAX //10) or
               (result == MAX //10 and digit >= MAX % 10)):
                
                return 0
            
            # IF the MIN integer
            if ((result < MIN // 10) or 
                (result == MIN // 10 and digit <= MIN % 10)):
                
                return 0
                
            result = (result * 10) + digit
            
        return result 
                
            
            
        
        
        
        
        
        