class Solution(object):
    def isHappy(self, n):
        # POA
        # 1) Understand what a Happy number is(DONE)
        # 2) implement a hashset to keep track of Happy Numbers that are used to avoid an infinite loop
        # 3) Code a function that will handle the math behind the squaring
        # 4) Do we ever visit a number twice?
        
        # STEP ONE create a HashSet of visited numbers when squarred and summed. 
        visited_num = set()
        
        # STEP TWO compute the sum of squares until a duplicate value is repeated
        
        while n not in visited_num:
            # add num to visited Hashset
            visited_num.add(n)
            # compute the sum of squares through a helper function 
            n = self.sumOfSquares(n)
            
            #  If we get a happy number.
            if n == 1:
                return True 
            
        # if the value was NOT one and was visited twice during the loop    
        return False 
     # Helper function to calculate the sum of Squares        
    def sumOfSquares(self, n):
        # TODO: Compute the square of digits
        
        # variable to store the output
        output = 0
        
        # sum the squares
        while n:
            # get the digit for the second square
            digit = n % 10
            # square the digit
            digit = digit ** 2
            # add the digit to output
            output+=digit
            # update n to find the next digit
            n = n // 10
            
        return output 
            
            
    
        
        
        
        
           
        