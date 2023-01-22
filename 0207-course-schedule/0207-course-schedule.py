class Solution(object):
    def canFinish(self, numCourses, prerequisites):
           # PLAN OF ATTACK(POA)
        # 1) Understand the problem
        # One way to go about it is use DFS and a dictionary or HashMap
        # the dictionary contains courses as the keys and preqs as values as the lists of courses
        # we can loop thhrough with recursion to check all possible combinations and from there check to see
        # if it is possible to complete the course.
        
        
        
        #STEP ONE: define a dictionary and map each course to a prereq. We're using List comprehension here.
        pre_Req_map =  {i:[] for i in range(numCourses)}
        
        # STEP TWO: grab each course and pre_req and append it to to course
        for crs, pre in prerequisites:
            pre_Req_map[crs].append(pre)
            
        # STEP THREE: create a set for all courses along the current DFS path.
        visitedCrsset = set()
        
        
       # STEP FOUR: nested function to handle recursive elements.
        def dfs(crs):
            # checking if the course is inside the visited set
            if crs in visitedCrsset:
                # if we have visited a course twice, we get a loop and therefore it is FALSE.
                return False 
            
            if pre_Req_map[crs] == []:
                # the course has NO preqs and can be completed
                return True
                
            visitedCrsset.add(crs)
            for pre in pre_Req_map[crs]:
                
                if not dfs(pre): return False 
                
            visitedCrsset. remove(crs)
            
            pre_Req_map[crs] = []
            
            return True 
        
        # call DFS for every course that we have
        for crs in range(numCourses):
            # if we can't complete any courses, return false
            if not dfs(crs): return False 
            
        # all courses are completed
        return True    
            
           
        
        
       
        