class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # STEP ONE: implement dynamic programming via  2D grid or Matrix
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        
        # STEP TWO: create a nested for loop iterating in REVERSE order
        for i in range(len(text1)-1,-1,-1):
            for j in  range(len(text2)-1,-1,-1):
                # if the characters MATCH
                if text1[i] == text2[j]:
                    # filling in the matrix and accounting for the diagonal
                    dp[i][j]  = 1 + dp[i+1][j+1]
                    
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
                    
        return dp[0][0]
                    
                
        
        
        # Solving this problem to better understand longest Palindronic subsequence
        
        