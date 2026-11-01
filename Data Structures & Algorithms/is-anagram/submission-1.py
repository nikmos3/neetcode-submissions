class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ''' 
        They are two string s & t, find the if they are both anagram return True if yes else False 
        '''


        '''
        1.) intialize dictionary
        2.) Loop s and t
        3.) check if same letters are present in both
        '''
        if len(s) != len(t):
            return False
        # anagramS = {}
        # anagramT = {}

        # for i in range(len(s)):
        #     anagramS[s[i]] = anagramS.get(s[i], 0) + 1
        #     anagramT[t[i]] = anagramT.get(t[i], 0) + 1
        # return anagramS == anagramT


        anagram = [0] * 26
        # print(anagram)

        for i in range(len(s)):
            anagram[ord(s[i]) - ord('a')] = anagram[ord(s[i]) - ord('a')] + 1
            anagram[ord(t[i]) - ord('a')] = anagram[ord(t[i]) - ord('a')] - 1

        # print(anagram)

        for val in anagram:
            if val != 0:
                return False
        return True
        
