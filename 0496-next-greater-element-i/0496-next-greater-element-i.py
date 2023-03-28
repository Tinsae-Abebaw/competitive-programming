class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[0]*len(nums1)
        for i in range(0,len(nums1)):
            nums2.append(0)
            for j in range(nums2.index(nums1[i]), len(nums2)-1):
                if nums2[j+1]>nums1[i]:
                    stack[i]=nums2[j+1]
                    break
                elif (nums1[i]==nums2[len(nums2)-1]):
                    stack[i]=-1
                else:
                    stack[i]=-1
        return stack