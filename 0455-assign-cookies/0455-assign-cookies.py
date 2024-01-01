class Solution(object):
    def findContentChildren(self, g, s):
        nums = len(s)
        if(nums==0):
            return 0
        g.sort()
        s.sort()
        
        sum = 0
        gi = len(g)-1
        si= len(s)-1
        
        while gi>=0 and si>=0:
                if(s[si]>=g[gi]):
                    sum+=1
                    gi-=1
                    si-=1
                else:
                    gi-=1
                    
        return sum
