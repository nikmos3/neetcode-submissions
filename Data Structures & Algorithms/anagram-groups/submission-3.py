class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        cache = defaultdict(list)
        

        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            cache[tuple(count)].append(s)

        # for res in cache.values():
        #     result.append(res)
        
        return list(cache.values())





        