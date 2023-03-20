class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        smaller=nums[0]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]<=nums[i]:
                    smaller=nums[j]
                    nums[i],nums[j]=nums[j],nums[i]
