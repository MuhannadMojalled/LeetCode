class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        p = 0
        t = 0
        for i in bank:
            ones = i.count("1")
            if ones:
                t +=p*ones
                p = ones
                
        return t