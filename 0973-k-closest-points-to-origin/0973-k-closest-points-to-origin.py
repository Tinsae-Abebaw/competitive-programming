import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance=0
        minheap = []
        output = []
        for x,y in points:
            distance=(x**2)+(y**2)
            minheap.append([distance,x,y])
        heapq.heapify(minheap)
        while k>0:
            distance,x,y=heapq.heappop(minheap)
            output.append([x,y])
            k-=1
        return output 