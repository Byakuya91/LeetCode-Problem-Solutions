class Solution:
    def partitionString(self, s: str) -> int:
        # STEP ONE: create a HashSet
        curCharSet = set()
        res = 1  # we know that the string,s won't be non-empty 
        
        # STEP TWO: iterate through every single character in the string
        for c in s:
            # checking if the char is in the set
            if c in curCharSet:
                # increment result and resetting the curChartSet
                res+=1
                curCharSet = set()
                
            curCharSet.add(c)
            
        return res
                
        
        
        