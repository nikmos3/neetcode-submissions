class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1 


        bucket = [[] for _ in range(len(nums) + 1)]
        
        for key,count in freq.items():
            bucket[count].append(key)
        res = []
        
        for i in range(len(bucket)-1,-1,-1):
            for j in bucket[i]:
                res.append(j)

                if len(res) == k:
                    return res


        

        
        