

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        queue = [(0,0)]
        count = 0
        if m > 1 and n >1:
            while queue:
                x, y = queue.pop()
                if (x >=0 and y >= 0) and (x < m and y < n):
                    if x == m-1 and y+1 == n-1:
                        count+=1
                    elif x+1 == m-1 and y == n-1:
                        count += 1
                    else:
                        if (x+1,y) not in queue:
                            queue.append((x+1,y))
                        if (x,y+1) not in queue:
                            queue.append((x,y+1))
        else:
            count += 1
        return count



if __name__ == "__main__":
    s = Solution()
    grid_size = (23,12)
    
    print(s.uniquePaths(grid_size[0],grid_size[1]))