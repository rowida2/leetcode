class Solution:
    def containsDuplicated(self,nums):

        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

nums=[1,2,3,1]
s=Solution()
if s.containsDuplicated(nums):
    print(True)
else:
    print(False)