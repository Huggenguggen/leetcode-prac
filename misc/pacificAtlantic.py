class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        vis = [[0 for _ in range(n)] for _ in range(m)]
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs1(i, j):
            vis[i][j] = 1
            for x, y in dir:
                if(0 <= i+x < m and 0 <= j+y < n and vis[i+x][j+y] == 0):
                    if(heights[i][j] <= heights[i+x][j+y]):
                        dfs1(i+x, j+y)         
        for i in range(m): dfs1(i, 0)
        for j in range(n): dfs1(0, j)
        self.ans = []
        def dfs2(i, j):
            if(vis[i][j] == 1):
                self.ans.append([i, j])
            vis[i][j] = 2
            for x, y in dir:
                if(0 <= i+x < m and 0 <= j+y < n and vis[i+x][j+y] != 2):
                    if(heights[i][j] <= heights[i+x][j+y]):
                        dfs2(i+x, j+y) 
        for i in range(m): dfs2(i, n-1)
        for j in range(n): dfs2(m-1, j)
        return self.ans