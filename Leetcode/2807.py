class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        outputorg=ListNode(0)
        output=outputorg
        while head:
            numa=head.val
            tempNode=ListNode(numa)
            output.next=tempNode
            output=output.next
            head=head.next
            if head != None:
                numb=head.val
                tempNode=ListNode(self.getGreatestCommonDvisor(numa,numb))
                output.next=tempNode
                output=output.next
        return outputorg.next

        
    def getGreatestCommonDvisor(self,numa,numb):
        maxD=1
        lessNum=numa
        if numa > numb:
            lessNum=numb
        for i in range(lessNum,1,-1):
            if numa%i == 0 and numb%i == 0:
                return i
        return maxD