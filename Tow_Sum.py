class Solutions:
    def towsum(self , nums , target):

        i=0
        y=target-nums[i]
        for i in nums:
            if nums[i]==y:
                return [i, i+1]
            else:
                i=i+1

s=Solutions()
nums=[2,7,11,15]
target=9
print(s.towsum(nums, target))               