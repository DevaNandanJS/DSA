class Solution(object):
    def isAnagram(self, s, t):
        c = False
        return sorted(s) == sorted(t)
