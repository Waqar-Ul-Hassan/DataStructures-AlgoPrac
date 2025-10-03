class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        inDegree = [0]*numCourses
        visited = []
        for pre, crs in prerequisites:
            adj[crs].append(pre)
            inDegree[pre]+=1
        
        q = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                q.append(i)
        
        while q:
            course = q.pop()
            visited.append(course)
            
            for nei in adj[course]:
                inDegree[nei] -= 1
                if inDegree[nei] == 0:
                    q.append(nei)
        return visited if len(visited) == numCourses else []
            