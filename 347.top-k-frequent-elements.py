class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for v in nums:
            freqs[v] = freqs[v] + 1 if v in freqs else 0
        nums = [v for v in freqs]
        heap = []
        for i in range(k):
            idx = len(heap)
            heap.append(nums[i])
            while idx > 0:
                p = (idx-1)//2
                if freqs[heap[p]] > freqs[heap[idx]]:
                    tmp = heap[p]
                    heap[p] = heap[idx]
                    heap[idx] = tmp
                    idx = p
                else:
                    break
        for i in range(k, len(nums)):
            if freqs[nums[i]] > freqs[heap[0]]:
                idx = 0
                child = idx * 2 + 1
                heap[0] = nums[i]
                while child < len(heap):
                    if child + 1 < len(heap) and freqs[heap[child + 1]] < freqs[heap[child]]:
                        child = child + 1
                    if freqs[heap[idx]] > freqs[heap[child]]:
                        tmp = heap[child]
                        heap[child] = heap[idx]
                        heap[idx] = tmp
                        idx = child
                        child = idx * 2 + 1
                    else:
                        break
        return heap
