from collections import deque

class Solution(object):
    def BFS(self, graph, rain):
        if graph[0][0] > rain:
            return None
        n = len(graph)
        q = deque()
        q.append((0,0))
        visited = [[-1]*n for _ in range(n)]
        visited[0][0] = 1
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        while q:
            x,y = q.popleft()
            if x == n-1 and y == n-1:
                return rain
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<n and 0<=ny<n and visited[nx][ny] == -1 and graph[nx][ny] <= rain:
                    q.append((nx,ny))
                    visited[nx][ny] += 1


    def swimInWater(self, grid):
        for i in range(len(grid)**2):
            if self.BFS(grid, i) != None:
                return i
        """
        :type grid: List[List[int]]
        :rtype: int
        """