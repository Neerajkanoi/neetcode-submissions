class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0]*n
        suffix=[0]*n
        pref[0]=1
        suffix[n-1]=1
        output=[0]*n
        for i in range(1,n,1):
            pref[i]=nums[i-1]*pref[i-1]
        for i in range(n-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i+1]
        for i in range(n):
           output[i]=pref[i]*suffix[i]
        return output 