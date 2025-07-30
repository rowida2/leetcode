class Solution:
    def getConcatenation(self, nums):
        n = len(nums)
        ans = [0] * (2 * n)
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        return ans

s = Solution()
nums = [1, 2, 1]
ans = s.getConcatenation(nums)
print(ans)