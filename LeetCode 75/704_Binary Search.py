class Solution:
    def search(self, nums, target: int) -> int:
        return self.binarySearch(nums,target,0,len(nums)-1)
    def binarySearch(self,nums,target,low,high):
        if low > high:
            return -1
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif low == high == mid:
            return -1

        if nums[mid] < target:
            return self.binarySearch(nums,target,mid+1,high)
        if nums[mid] > target:
            return self.binarySearch(nums,target,low,mid)


if __name__ == "__main__":
    s =Solution()
    #data = [1,4,6,7,8,10,15,14,20,25]
    data = [-1,0,3,5,9,12]
    print(s.search(data,2))