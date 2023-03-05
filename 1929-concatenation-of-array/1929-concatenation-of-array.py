class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # STEP ONE: create an empty array
        answer = []
        
        
        
        # STEP TWO: take every number in nums and append it to answer and run this two times. 
        # Addendum: the reason for i in range is that it is a generic solution. You can modiy 2 to be any n to have the loop
        # run n number of times.
        
        for i in range(2):
            for n in nums:
                answer.append(n)
        return answer    
        
        
        
        #1) Understand the problem(DONE)
        # 2) Code up the soolution
        