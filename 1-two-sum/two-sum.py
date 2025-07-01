class Solution(object):
    def twoSum(self, nums, target):
        c = []
        for i in range (len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    c.append(i)
                    c.append(j)
        return c