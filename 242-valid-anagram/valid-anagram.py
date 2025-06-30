class Solution(object):
    def isAnagram(self, s, t):
        c = False
        a = list(s)
        b = list(t)
        return sorted(a) == sorted(b)
