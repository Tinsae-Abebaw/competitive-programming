class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        j=0
        answer=[0]*(nums.count(target))
        nums.sort()
        for i in range(0, len(nums)):
            if nums[i]==target:
                answer[j]=i
                j+=1  
        return answer