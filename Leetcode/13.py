class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roamnMap={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        orderList=["I","V","X","L","C","D","M"]
        sign=1
        lastIdx=1
        result=0
        for c in s:
            newIdx=roamnMap[c]
            if newIdx > lastIdx:
                sign=-1
            result+=(sign*newIdx)
            if result < 0:
                result=result*-1
            sign=1
            lastIdx=newIdx
        print(result)

s=Solution()
print(s.romanToInt("IX"))