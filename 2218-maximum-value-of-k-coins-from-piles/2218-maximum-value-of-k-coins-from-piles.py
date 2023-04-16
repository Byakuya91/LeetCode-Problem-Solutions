class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        # STEP ONE: get the number of piles of coins and a Cache
        n = len(piles)
        # this is a 2D array using the DFS loop we've seen below 
        dp = [[-1] * (k+1) for _ in range(n)]
        
        # STEP TWO: implement DFS. i keeps tracks of the piles and coins is how many coins can be collected
        def dfs(i,coins):
            # SUB STEP ONE: define BASE CASES
            # going out of bounds
            if i == n:
                return 0
            # if the values exist inside the cache
            if dp[i][coins] != -1:
                return dp[i][coins]
            
            # SUB STEP TWO: Skipping the CURRENT pile
            dp[i][coins] = dfs(i+1,coins)
            
            # SUB STEP THREE: Collect from the CURRENT pile
            curPile = 0
            # We're taking into account of k coins. If k =3 and curPile = 10 we can only take 3 coins. 
            for j in range(min(coins, len(piles[i]))):
                curPile+=piles[i][j]
                dp[i][coins] = max(dp[i][coins],   curPile +dfs(i+1,coins - j - 1))
                    
            return dp[i][coins]
                
                
                
                
            
            
            
            
        return dfs(0,k)
            
        
        
        
        
        
        """
        Plan of Attack
        1) Understand the problem(DOING)
        2) Implement Memoization and Recursion via DPS
        
        
        
        """
        