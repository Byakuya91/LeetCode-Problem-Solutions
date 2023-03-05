class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # STEP ONE: create a merge function
        def merge(arr,L,M,R):
             # create copies of the left and right halves of the array
            left,right = arr[L:M+1], arr[M+1:R+1]
            
            # create pointers for the array
            i,j,k = L,0,0
            
            # Merge process: 
            
            # sort the two halves individuall
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                     # put the left value into the array
                    arr[i] = left[j]
                    # increment the pointers
                    j+=1
                    
                else:
                    # right side of the split array
                    arr[i] = right[k]
                    k+=1
                i+=1
            
            # if the values are still prevalent in the left and right. 
            while j < len(left):
                nums[i] = left[j]
                j+=1
                i+=1
                
            while k < len(right):
                nums[i] = right[k]
                k+=1
                i+=1
                
        # STEP TWO: create a function to handle the Merge sort        
        def mergeSort(arr,l,r):
            # BASE CASE
            if l == r:
                return arr
            
             # grab the middle of the array
            m = (l+r) //2
            
            # Recursively run the MergeSort on left and right halves AND the merge function for the array
            mergeSort(arr,l,m)
            
            mergeSort(arr, m+1, r)
            
            merge(arr,l,m,r)
            
            return arr
        
        return mergeSort(nums,0,len(nums)-1)
                
       
            
            
        
        
        