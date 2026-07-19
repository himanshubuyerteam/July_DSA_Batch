class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.psum = [0]*len(nums)

        self.psum[0]=nums[0]
        for i in range(1,len(nums)):
            self.psum[i]= self.psum[i-1]+nums[i]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.psum[right]
        return self.psum[right]-self.psum[left-1]


    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        psum = [0]*n
        psum[0] = nums[0]

        for i in range(1,n):
            psum[i]=psum[i-1]+nums[i]

        
        for k in range(n):
            if k==0:
                lsum = 0
                rsum = psum[n-1]-psum[0]
            else:
                lsum = psum[k-1]
                rsum = psum[n-1]-psum[k]
            
            if lsum==rsum:
                return k
        return -1

    def trap(self, height: List[int]) -> int:
        n = len(height)

        pmax = [0]*n
        smax = [0]*n

        pmax[0]=height[0]
        for i in range(1,n):
            pmax[i]=max(pmax[i-1],height[i])


        smax[n-1]=height[n-1]
        for i in range(n-2,-1,-1):
            smax[i]=max(smax[i+1],height[i])

        water = 0

        for i in range(n):
            potenialWater = min(pmax[i],smax[i])
            water+=potenialWater-height[i]

        return water

    def productExceptSelf(arr):
        n = len(arr)

        pp = [0] * n // LP
        sp = [0] * n  //RP

        pp[0] = arr[0]
        for i in range(1, n):
            pp[i] = pp[i - 1] * arr[i]

        sp[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            sp[i] = sp[i + 1] * arr[i]

        fans = [0] * n

        fans[0] = sp[1]
        fans[n - 1] = pp[n - 2]

        for i in range(1, n - 1):
            fans[i] = pp[i - 1] * sp[i + 1]

        return fans