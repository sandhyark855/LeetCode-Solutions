class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        smallest=min(nums)
        largest=max(nums)
        num_set=set(nums)
        result=[]
        for i in range(smallest,largest+1):
            if i not in num_set:
                result.append(i)
        return result        
        