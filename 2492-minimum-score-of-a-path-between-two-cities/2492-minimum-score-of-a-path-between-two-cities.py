class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # Understand the problem(DONE)
        # Utilize Depth First Search
        
        # STEP ONE: create an adjacencies list that is a hashmap
        adj=defaultdict(list)
        
         # STEP TWO: build the adj list: dst =  destination, dist = distance, src = source
        for src,dst,dis in roads:
            adj[src].append((dst,dis))
            adj[dst].append((src,dis))
         # STEP THREE: utilize depth first search
        def dfs(i):
            # Base case
            if i in visit:
                return
            visit.add(i)
            # nonlocal because answer needs to be accessed but it is in a for loop and disclosed. 
            nonlocal answer
            for nei,dis in adj[i]:
                answer=min(answer,dis)
                dfs(nei)
        visit,answer=set(),float('inf')
        # STEP FOUR: calling dfs function.
        dfs(n)
        return answer
           
        
       
        