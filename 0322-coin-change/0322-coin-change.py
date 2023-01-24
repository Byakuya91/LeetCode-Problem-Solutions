class Solution(object):
    def coinChange(self, coins, amount):
        #POA(Plan of ATTACK)
        # 1) Understand the problem(DONE)
        # 2) Brush up on Depth First Search(DPS)(DONE)
        # 3) Create a visual of the problem(DONE)
        # 4) Psuedo-code the problem(DONE)
        # 5) Intergrate the solution(shown below)(DONE)
        
        
        
        # STEP ONE: create a dynamic programming array
        # amount + 1 is that we are starting from zero all the way to the amount.
        # amount + 1 inside a list is a max value 
        dpArr = [amount+1] * (amount+1)
        
        #STEP TWO: define a base case to indicate how many coins 
        dpArr[0] = 0
        
        # STEP THREE: iterate through every value in dpArr. The range is because we are going from bottom up when Depth First Searching
        for a in range(1,amount+1):
            # iterate through every coin
            for c in coins:
                # if the amount minus coins is NOT negative
                if a -c >= 0:
                    # the a-c in dpArr comes from taking the amount and minusing it from the coin.
                    # This is known as a recurrence relation
                    dpArr[a] = min(dpArr[a], 1+ dpArr[a-c])
                    
        # Dealing with an Edge case where the amount is NOT the defaul value.
        # Other wise we return a -1, meaning we could NOT compute the given amount with the coins. 
        return dpArr[amount] if dpArr[amount] != amount+1 else -1
        
        
       
        