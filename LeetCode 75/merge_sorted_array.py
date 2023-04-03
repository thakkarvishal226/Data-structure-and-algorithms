class Solution:
   def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]


if __name__ == "__main__":
    s = Solution()
    num1 = [1,2,3,0,0,0]
    num2= [2,5,6] 
    s.merge(num1,3,num2,3)
    print(num1)