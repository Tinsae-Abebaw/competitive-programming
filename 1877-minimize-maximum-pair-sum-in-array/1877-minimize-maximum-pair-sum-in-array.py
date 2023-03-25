class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        maximum_sum=0
        nums.sort()
        while j>i:
            if nums[i]+nums[j]>maximum_sum:
                maximum_sum = nums[i]+nums[j]
            j-=1
            i+=1
        return maximum_sum