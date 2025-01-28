# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        output=ListNode(0)
        outP=output
        carry=0
        while l1 or l2 or carry > 0:
            val1=val2=0
            if l1:
                val1=l1.val
                l1=l1.next
            if l2:
                val2=l2.val
                l2=l2.next
            s=val1+val2+carry
            carry=s//10
            node=ListNode(s%10)
            outP.next=node
            outP=outP.next
        return output.next
        