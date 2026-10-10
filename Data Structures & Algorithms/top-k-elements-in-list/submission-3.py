class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        res = []
        for i in freq:
            res.append(i)
        res.sort(key=freq.get)
        return res[-k:]