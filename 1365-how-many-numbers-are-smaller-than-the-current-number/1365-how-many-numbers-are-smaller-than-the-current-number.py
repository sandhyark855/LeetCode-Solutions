class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                if nums[j]<nums[i]:
                    count+=1
            num.append(count)        
        return num        

        