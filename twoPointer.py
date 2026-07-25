def twoSum(self, nums: List[int], target: int) -> List[int]:

        i=0
        j=len(nums)-1
        while(i<j):
            curr_sum = nums[i]+nums[j]

            if curr_sum == target:
                return [i,j]
            elif curr_sum>target:
                j-=1
            else:
                i+=1
        return [-1,-1]



def pushZerosToEnd(self, arr):
    	# code here
    	i = 0
        j = 0
        n = len(arr)
        while(i<n):
            if arr[i]!=0:
                self.swap(arr,i,j)
                i+=1
                j+=1
            else:
                i+=1
        return
    
    def swap(self,arr,i,j):
        temp = arr[i]
        arr[i]=arr[j]
        arr[j]=temp

def maxArea(self, arr: List[int]) -> int:
        i = 0
        j = len(arr)-1

        max_water = 0

        while i<j :
            height = min(arr[i],arr[j])
            widht = j-i
            water = height * widht

            max_water = max(water,max_water)

            if arr[i]>arr[j]:
                j-=1
            else:
                i+=1
        return max_water


def reverseArray(self, arr,si,ei):
        # code here
        i  = si
        j = ei
        while i<j:
            self.swap(arr,i,j)
            i+=1
            j-=1
            
    def swap(self,arr,i,j):
        temp = arr[i]
        arr[i]=arr[j]
        arr[j]=temp


    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k%n
        if(k==0):
            return
        self.reverseArray(nums,0,n-1)
        self.reverseArray(nums,0,k-1)
        self.reverseArray(nums,k,n-1)