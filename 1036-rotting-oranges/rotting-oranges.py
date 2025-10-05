class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                    visited.add((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        maxTime = 0
        while q:
            r, c, t = q.popleft()
            maxTime = max(maxTime, t)
            for dx, dy in directions:
                if 0 <= r+dx < rows and 0 <= c+dy < cols and (r+dx, c+dy) not in visited and grid[r+dx][c+dy] == 1:
                    visited.add((r+dx, c+dy))
                    q.append((r+dx, c+dy, t+1))
                    fresh -= 1
        
        return maxTime if 0 == fresh else -1
        
