class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        '''
        we must tranverse  all the words and separate them and 
        group them if they are anagram of each other
        '''
        res = defaultdict(list)

        for stri in strs:
            anagram = [0] * 26
            for s in stri:
                anagram[ord(s) - ord('a')] += 1
            res[tuple(anagram)].append(stri)
        return list(res.values())



            
        