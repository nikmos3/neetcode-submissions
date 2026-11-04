class Solution:

    def encode(self, strs: List[str]) -> str:
        encd = ""
        if not strs:
            return ""

        for s in strs:
            encd += str(len(s)) + '#' + s

        return encd
        

    def decode(self, s: str) -> List[str]:
        res = []
        print(s)
        len_str = ''
        idx = 0
        #       5#Hello
        while len(s) > idx:
            if s[idx].isdigit():
                len_str += s[idx]
                
            elif s[idx] == '#':
                res.append(s[idx + 1:idx + int(len_str) + 1])
                idx = idx + int(len_str)
                len_str = ''

            idx += 1
        return res if res else []
            

            




