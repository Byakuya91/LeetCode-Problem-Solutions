class Solution:
    def mySqrt(self, x: int) -> int:
         # Understand the problem(DONE)
        #) Binary Search could potentially be used.
        # Speficically cutting the search range in half and comparing the median to the value.
        # if GREATER than the median, we discard the latter half and go to the former half, comparing the previous val before
        # median and from there get the result. 
        
        # STEP ONE: create a search space through l,r pointers and result
        l,r = 0,x
        res = 0
        
        # STEP TWO: run the Binary search as a WHILE loop.
        while l <=r:
            # defining the median of the search range.
            m = l + ((r-l)//2)  # this will prevent over-flow when searching
            
            # check if the median is greater than the square of x:
            if m**2 > x:
                # reduce the search space
                r = m -1
            elif  m**2 < x:
                # searching the left side
                l = m + 1
                res = m
            # checking if m**2 is equal to x
            else:
                return m
            
        return res
        
        
        
       
        