class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        keyMap={}
        for i,num in enumerate(nums):
            newTarget=target - num
            print(newTarget,keyMap.items())
            tempResult=[i]
            if newTarget in keyMap:
                print("I am here")
                tempResult.append(keyMap[newTarget][0])
                return tempResult
            if num in keyMap:
                keyMap[num].append(i)
            else:
                keyMap[num]=[i]

s=Solution()
print(s.twoSum([1,1,1,1,1,4,1,1,1,1,1,7,1,1,1,1,1],11))