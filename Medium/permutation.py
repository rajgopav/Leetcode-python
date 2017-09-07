class Solution():
    def permute(self, nums):
        result = []
        visited = [False] * len(nums)
        self.permuteRec(result, visited, [], nums)
        return result

    def permuteRec(self, result, visited, curr, nums):
        if len(curr) == len(nums):
            result.append(curr + [])
            return result

        for i in xrange(len(nums)):
            if not visited[i]:
                visited[i] = True
                curr.append(nums[i])
                self.permuteRec(result, visited, curr, nums)
                curr.pop()
                visited[i] = False

if __name__ == "__main__":
    print Solution().permute([1, 2, 3])