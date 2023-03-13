class Solution:
    def addDigits(self, num: int) -> int:

        # str_num = str(num)
        
        # STEP ONE: convert the nums to a string and loop through it
        
        while num // 10 !=0:
            # STEP TWO: convert the num into a string 
            num = str(num)
            # STEP TWO convert values to a list of nums and add them up
            num = sum(map(int,list(num)))
            
        return num
            
            
            
        
        
        # Understand the problem(DONE)
        # Code the solution(ONGOING)
       
       