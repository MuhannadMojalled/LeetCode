class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
                
        b = bin(n)[2:]
        lis = []
        for i in b:
            lis.append(i)
            
        for j in range(len(lis)):
            if lis[j] =='0':
                lis[j]='1'
            else :
                lis[j]='0'
        reverseds = ""
        for k in lis:
            reverseds +=k
        output = int(reverseds,2)
        return output