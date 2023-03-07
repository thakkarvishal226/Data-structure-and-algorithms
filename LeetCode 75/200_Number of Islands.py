class Solution:
    def numIslands(self, grid) -> int:
        rows = len(grid)
        cols = len(grid[0])

        islandCount = 0

        def DFS(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return
            
            if grid[row][col] != '1':
                return 
            
            grid[row][col] = 'V'
            DFS(row - 1,col)
            DFS(row + 1,col)
            DFS(row,col - 1)
            DFS(row, col + 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    DFS(i,j)
                    islandCount += 1
        return islandCount
if __name__  == "__main__":
    s = Solution()
    data = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]]
    print(s.numIslands(data))