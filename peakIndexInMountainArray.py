A = [0,2,1,0]

def peakIndexInMountainArray(A):
        """
        :type A: List[int]
        :rtype: int
        """
        maxi = 0
        index = 0
        for i in range(len(A)):
            #print(i, A[i])
            if A[i] > maxi:
                maxi = A[i]
                index = i
                print("max and index",maxi, index)
        return index

print(peakIndexInMountainArray(A))
