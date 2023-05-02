class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # Methodology
        # I avoided overflow and having to multiple the elements within the input array
        
        
        # STEP ONE: create a variable that counts all the negative numbers
        neg = 0
        
        # STEP TWO: iterate through the num input array
        for n in nums:
            # checking if the number is zero
            if n == 0:
                return 0
            #counting up the number of negative numbers
            neg+=(1 if n <0 else 0)
            
        return -1 if neg % 2 else 1
            
        
            
        