# Max SubArray Sum in K Size

# Brute Force

def maxSlidingWindow(arr,k):
    n = len(arr)
    maxSum = 0

    for i in range(n-k+1):
        curr_sum = 0
        for j in range(k)
            curr_sum+=arr[j+i]
        maxSum = max(maxSum,curr_sum)
    return maxSum

def maxSlidingWindow(arr,k):
    curr_sum = sum(arr[:k])
    max_sum = curr_sum

    for i in range(k,len(arr)):
        curr_sum = curr_sum+arr[i]-arr[i-k]
        max_sum = max(max_sum,curr_sum)
    return max_sum

def maxAvg(arr,k):
    curr_sum = sum(arr[:k])
    max_sum = curr_sum

    for i in range(k,len(arr)):
        curr_sum = curr_sum+arr[i]-arr[i-k]
        max_sum = max(max_sum,curr_sum)
    return max_sum/k

def minLengthSlidingWindow(arr,target):
    i = 0
    j = 0
    ansLen = float('inf')
    curr_sum = 0
    for i in range(len(arr)):
        curr_sum = curr_sum+arr[i]

        while curr_sum>=target:
            curr_len = i-j+1
            ansLen = min(ansLen,curr_len)
            curr_sum = curr_sum-arr[j]
            j+=1


    return 0 if ansLen == float('inf') else ansLen
    


def longestWindowNoDuplicate(self,s,t):
    i = 0
    j = 0
    duplicate = False
    anslen = float('-inf')

    freq = [0]*256

    while i<len(s):
        ch = ord(s[i])

        if freq[ch] == 1:
            duplicate = True

        freq[ch]+=1
        i+=1

        while duplicate
            ch2 = ord[s[j]]
            if freq[ch2]==2
                duplicate = False
            freq[ch2]-=1
            j+=1
    
        curr_len = i-j+1
        ansLen = max(curr_len,ansLen)
    return ansLen
            

