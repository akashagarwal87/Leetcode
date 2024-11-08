class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        newNum=0
        orgNum=x
        while x > 0:
            mod=x%10
            x=x//10
            newNum=newNum*10+mod
            print(newNum)
        
        if newNum == orgNum:
            return True
        return False
    
s=Solution()
print(s.isPalindrome(10))