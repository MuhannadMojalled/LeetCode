class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        have = Counter(nums)
        for i in have:
            if have[i]==1:
                return -1
            else:
                count+= have[i]//3 + (have[i]%3!=0)
        return count