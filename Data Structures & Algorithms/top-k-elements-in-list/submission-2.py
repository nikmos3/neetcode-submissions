class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)]
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        
        for num, freq in count.items():
            buckets[freq].append(num)
        res = []
        for arr in range(len(buckets)-1,-1,-1):
            while buckets[arr] and k > 0:
                res.append(buckets[arr].pop())
                k -= 1
        return res



        

        
        