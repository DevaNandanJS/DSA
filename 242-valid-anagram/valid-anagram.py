class Solution(object):
    def isAnagram(self, s, t):
        c = False
        a = list(s)
        b = list(t)
        a.sort()
        b.sort()
        if  a == b:
            c = True
        return c
