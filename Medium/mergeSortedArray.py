class Solution():
    def mergeSortedArray(self, nums1, m, nums2, n):
        last, i, j = m + n - 1, m - 1, n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[last] = nums1[i]
                last, i = last - 1, i - 1
            else:
                nums1[last] = nums2[j]
                last, j = last - 1, j - 1

        while j >= 0:
            nums1[last] = nums2[j]
            last, j = last - 1, j - 1

if __name__ == '__main__':
    Solution().mergeSortedArray([1, 3, 5, 0, 0, 0, 0], 3, [2, 4, 6, 7], 4)