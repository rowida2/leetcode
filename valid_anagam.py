from collections import Counter

class Solution:
    def validation(self, s, t):
        return Counter(s) == Counter(t)

c = Solution()
s = "anagram"
t = "margana"
if c.validation(s, t):
    print(True)
else:
    print(False)
