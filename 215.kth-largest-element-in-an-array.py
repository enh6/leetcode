class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(k):
            idx = len(heap)
            heap.append(nums[i])
            while idx > 0:
                p = (idx-1)//2
                if heap[p] > heap[idx]:
                    tmp = heap[p]
                    heap[p] = heap[idx]
                    heap[idx] = tmp
                    idx = p
                else:
                    break
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                idx = 0
                child = idx * 2 + 1
                heap[0] = nums[i]
                while child < len(heap):
                    if child + 1 < len(heap) and heap[child + 1] < heap[child]:
                        child = child + 1
                    if heap[idx] > heap[child]:
                        tmp = heap[child]
                        heap[child] = heap[idx]
                        heap[idx] = tmp
                        idx = child
                        child = idx * 2 + 1
                    else:
                        break
        return heap[0]



