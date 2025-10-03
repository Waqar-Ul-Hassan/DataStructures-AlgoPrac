class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        inDegree = [0]*numCourses
        visited = 0
        for pre, crs in prerequisites:
            adj[crs].append(pre)
            inDegree[pre]+=1
        
        q = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        
        while q:
            course = q.pop()
            visited+=1
            
            for nei in adj[course]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    q.append(nei)
        return visited == numCourses
            