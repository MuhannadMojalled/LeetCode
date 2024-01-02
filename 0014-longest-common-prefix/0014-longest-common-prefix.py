class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        op = ""
        strs.sort()
        fw = strs[0]
        lw = strs[-1]
        
        for i in range(len(fw)):
            if fw[i] == lw[i]:
                op +=fw[i]
            else: break
        return op
        