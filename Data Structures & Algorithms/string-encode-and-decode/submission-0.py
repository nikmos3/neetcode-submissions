class Solution:

    def encode(self, strs: List[str]) -> str:
        newstring = ""

        for stri in strs:

            newstring += str(len(stri)) + '#' + stri
        return newstring
        


    def decode(self, s: str) -> List[str]:
        decodString = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decodString.append(s[i:j])
            i = j
        return decodString

            

            
        