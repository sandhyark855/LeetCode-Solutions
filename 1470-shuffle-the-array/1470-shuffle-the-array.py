class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        num=[]
        for i in range(n):
            num.append(nums[i])
            num.append(nums[i+n])
        return num    

        