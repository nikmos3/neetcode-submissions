class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq = defaultdict(int)

        # for num in nums:
        #     freq[num] += 1 


        # bucket = [[] for i in range(len(nums) + 1)]

        # for key,count in freq.items():
        #     bucket[count].append(key)
        # res = []
        
        # for i in range(1, k + 1):
        #     for j in bucket[i]:
        #         res.append(j)

        # return res

        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1

        freq = [[] for _ in range(len(nums) + 1)]


        for n,f in counter.items():
            freq[f].append(n)


        res = []

        for i in range(len(freq)-1,-1,-1):
            
            for j in freq[i]:
                res.append(j)

                if len(res) == k:
                    return res
        