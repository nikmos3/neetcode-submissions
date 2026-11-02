class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        result = ""
        present = defaultdict(int)

        for i in range(len(strs)-1):
            for j in range(min(len(strs[i]), len(strs[i+1]))):
                if strs[i][j] == strs[i+1][j]:
                    present[j] += 1
                else:
                    break


        for k,v in present.items():

            if v == len(strs) - 1:
                result += strs[0][k]
           
        return result





                    
            



                        




                













        