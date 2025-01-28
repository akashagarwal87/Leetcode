class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        output=""
        for i in date.split("-"):
            output=self.convert2Bin((i))
            output+="-"
        return output
        
    def convert2Bin(self,s):
        output=0
        num=0
        for i in s:
            num=num*10+int(i)
        while num > 1:
            output=output*10+(num%2)
            num=num//2
        return output