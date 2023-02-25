# time: O(2^40) > 10^8. so TLE.

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        ans= [float('inf')]
        self.helper(0, nums, goal, ans)
        return ans[0]
    
    def helper(self, i, nums, goal, ans):
        if i== len(nums):
            ans[0]= min(ans[0], abs(goal))
            return 
        self.helper(i+1, nums, goal- nums[i], ans)   # when we include the curr ele.
        self.helper(i+1, nums, goal, ans)     # when we don't include the current ele.


# time: O(2^20) will work since < 10^8.
# Till 2^26 will work fine.

# logic: Divide nums in half. Collect subsequence subs of the two halves respectively and 
# search for a combined sum that is closest to given target.
# Time complexity O(2^(N/2))
# Space complexity O(2^(N/2))

# also we can say little intuition is taken from the 'minimum sum partition'. (DP Q)
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
    
        def dfs(i, cur_sum, nums, ans):
            if i== len(nums):
                ans.append(cur_sum)
                return
            dfs(i+1, cur_sum + nums[i], nums, ans)   # when we include the curr ele.
            dfs(i+1, cur_sum, nums, ans)     # when we don't include the current ele.
        
        n= len(nums)
        sum1= []  # will store the all possible sum of subsequences till first half.
        sum2= []  # will store the all possible sum of subsequences till second half.
        dfs(0, 0, nums[:n//2], sum1)
        dfs(0, 0, nums[n//2:], sum2)

        # now traverse any of the array and sort the another half to find the closest sum of each ele in traversing array.
        res= float('inf')
        sum2.sort()
        for num in sum1:
            new_goal= goal - num
            # find the closest num of 'new_goal' in another array and there can be two possible values 1) ceiling and 2) floor
            i= bisect_left(sum2, new_goal)
            # first calculating the diff with ceiling value.
            if i < len(sum2):
                res= min(res, abs(new_goal - sum2[i]))
            # Now calculating the diff with floor value.
            if i > 0:
                res= min(res, abs(new_goal - sum2[i-1]))
        
        return res