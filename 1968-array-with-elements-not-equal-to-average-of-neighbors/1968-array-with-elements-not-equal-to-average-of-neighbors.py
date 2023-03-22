class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        i=1
        while i < len(nums)-1:
            if nums[i] == (nums[i-1]+nums[i+1])/2:
                nums.append(nums[i])
                nums.remove(nums[i])
                i=1
                continue
            i+=1
        return nums