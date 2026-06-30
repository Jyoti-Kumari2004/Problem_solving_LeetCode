class Solution:
    def __init__(self):
        self.ans=0
    def reversePairs(self, arr: List[int]) -> int:
        self.mergeSort(arr,0,len(arr)-1)
        return self.ans
    def mergeSort(self,arr, left, right):
        if left < right:
            mid = (left + right) // 2
    
            self.mergeSort(arr, left, mid)
            self.mergeSort(arr, mid + 1, right)
            self.merge(arr, left, mid, right)
        
    def merge(self,arr,l,m,r):
        n1=m-l+1
        n2=r-m
        
        L=[]
        for i in range(n1):
            L.append(arr[l+i])
        R=[]
        for i in range(n2):
            R.append(arr[m+1+i])
        i=0
        j=0
        k=l
        while i<n1 and j<n2:
            if L[i]>2*R[j]:
                self.ans+=(n1-i)
                j+=1
            else:
                i+=1
        i=0
        j=0
        k=l
        while i<n1 and j<n2:
            if L[i]<=R[j]:
                arr[k]=L[i]
                i+=1
                k+=1
            else:
                arr[k]=R[j]
                j+=1
                k+=1
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
            
        
        
        