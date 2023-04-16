from collections import defaultdict
class Solution:
    ''' 
         Plan of attack
         1) Brute Force approach where we iterate through each sequence
         2) utilizing Caching to store the values
         3) Utilizing Depth First Search and recursion to go through the values 
         4) Reseach what Caching is and Memoization(DONE)
         
         5) Avoid a timeout in Leetcode by precounting the string combinations and do some precounting.
        
        
        '''
    def numWays(self, words: List[str], target: str) -> int:
        # BEFORE ATTEMPTING MAKING THE PROBLEM EASY TO READ THROUGH OUTPUT
        mod = 10**9 + 7 # 
        
        # STEP ONE: Precomputation step where we count all the words
        
        # create a dictionary to store the values
        cnt = defaultdict(int)   # we're mapping the (index,char) -> count among all the words
        
        for w in words:
            for i,c in enumerate(w):
                cnt[(i,c)]+=1
                
        # STEP TWO: DFS function
        # i = index of target, k = index of a word[j][k]
        
        # DEFINE A CACHE
        dp = {}   # mapping i, k => numWays to build target word
        
        
        def dfs(i,k):
            # BASE CASES
            if i == len(target):
                return 1
            # if we go through the word and not build any characters
            if k == len(words[0]):
                return 0
            # checking results are inside the cache 
            if (i,k) in dp:
                return dp[(i,k)]
            
            c = target[i]
            dp[(i,k)] = dfs(i, k+1)  # skip the position
            dp[(i,k)] +=  cnt[(k,c)]  * dfs(i+1,k+1)
            
            return dp[(i,k)] % mod
        
            
        return dfs(0,0)
            
                
            
                
        
        
        
        
        
        
        
        