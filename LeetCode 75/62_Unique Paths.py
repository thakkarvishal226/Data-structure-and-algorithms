

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        print(row)
        for _ in range(m-1):
            newrow = [1] * n
            for j in range(n-2,-1,-1):
                newrow[j] = row[j] + newrow[j+1]
            row = newrow
            print(row)
        return row[0]


if __name__ == "__main__":
    s = Solution()
    grid_size = (30,12)
    
    print(s.uniquePaths(grid_size[0],grid_size[1]))