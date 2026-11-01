class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1,nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        if len(A) > len(B):
            A,B = B,A 
        l,r = 0, len(A) - 1

        while True:
            m1 = (l+r) // 2
            m2 = half - m1 - 2

            Aleftmin = A[m1] if  m1 >= 0else float('-inf')
            Arightmax = A[m1 + 1] if (m1 + 1) <len(A) else float('inf')
            Bleftmin = B[m2] if m2 >=0 else float('-inf')
            Brightmax = B[m2 + 1] if (m2+1) < len(B) else float('inf')

            if Aleftmin <= Brightmax and Bleftmin <= Arightmax:
                if total % 2:
                    return min(Arightmax,Brightmax)
                return (max(Aleftmin,Bleftmin) + min(Arightmax,Brightmax)) / 2
            elif Aleftmin > Brightmax:
                r = m1 - 1
            else:
                l = m1 + 1
