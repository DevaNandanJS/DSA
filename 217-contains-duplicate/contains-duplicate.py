class Solution(object):
    def containsDuplicate(self, nums):
        ans = False
        s = set()
        for i in nums:
            s.add(i)
        if len(s) != len(nums):
            ans = True
        return ans