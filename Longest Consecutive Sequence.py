# LeetCode 128. Longest Consecutive Sequence
# Difficulty: Medium

class Solution:
    def longestConsecutive(self, nums):

        long=0
        num_set=set(nums)

        for n in num_set:
           
            if (n-1) not in num_set:
                length = 1

                while (n+length) in num_set:
                    length +=1
                long=max(long, length)
        return long

