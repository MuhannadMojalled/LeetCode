class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        list = []
        for i in range(l-1):
            for j in range(i+1,l):
                if nums[i] + nums[j] == target:
                    list.append(i)
                    list.append(j)
        return list         