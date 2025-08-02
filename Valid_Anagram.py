class Solution:
    def validation(self , s, t):
        s=list(s)
        t=list(t)
        for i in s:
            if i in t:
               t.remove(i)
            else:
                return False
        return True

c=Solution()
s="anagram"
t="nagaram"
if c.validation(s,t):
    print(True)
else:
    print(False)
