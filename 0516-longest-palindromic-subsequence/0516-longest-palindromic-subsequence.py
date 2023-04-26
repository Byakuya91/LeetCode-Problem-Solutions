class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # NEW SOLUTION USING Dynamic programming 
        n = len(s)
        dp = [[0]*n for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return dp[0][n-1]

   # OLD SOLUTION TIME OUT LIMIT
# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         cache = {}

#         # We will approach this recursively
#         # STEP ONE: create a dfs function with l and r pointers as parameters
#         def dfs(l,r):
#             # BASE case: 
#             # when l or right is out of bounds
#             if l < 0 or r == len(s):
#                 return 0
#             # if l and r are inside the cache
#             if (l,r) in cache:
#                 #  value inside the cache
#                 return cache[(l,r)]
            
#             # if both characters in the pointers match each other
#             if s[l] == s[r]:
                
#                 cache[(l,r)] = length = 1 if l == r else 2 + dfs(l+1,r-1)
                
#             else:
#                 cache[(l,r)] =  max(dfs(l+1,r), dfs(l,r-1))
                
#             return cache[(l,r)]
                
#         # Loop through every position in the input string
#         for i in range(len(s)):
#             dfs(i,i)  # Odd length palindromic sub-sequences
#             dfs(i,i+1)  # Even length palindromic sub-sequences
            
#         return max(cache.values())

            
            
        