# The isBadVersion API is already defined for you.

def isBadVersion(version: int) -> bool:
    return True if version > 3 else False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        return self.binarySearch(0,n)
    def binarySearch(self,low,high):
        mid = (low + high) // 2
        if isBadVersion(mid - 1):
            return self.binarySearch(low, mid - 1)
        elif isBadVersion(mid):
            return mid
        else:
            return self.binarySearch(mid+1, high)





if __name__ == "__main__":
    s = Solution()
    n = 5
    print(s.firstBadVersion(n))