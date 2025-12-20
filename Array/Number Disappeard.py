class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result = []
        count = [0] * (n+1)

        for num in nums:
            count[num] +=1
        for i in range (1, n+1):
            if count[i]==0:
                result.append(i)
        return result
