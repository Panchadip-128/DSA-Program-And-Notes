# time= space= O(n)
# logic in code only.

class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        n= len(nums)
        maxTillIndex= [nums[0]]  # will store the max ele till index 'i'.
        for i in range(1, n):
            curMax= max(nums[i], maxTillIndex[-1])  # only we need to compare with last ele because that will the max till index 'i-1'.
            maxTillIndex.append(curMax)
        # now making the conver array.
        conver= [0]*n
        for i in range(n):
            conver[i]= nums[i] + maxTillIndex[i]
        # finding the answer array , just score of array only.
        # ans= the prefix sum of arr 'conver'
        ans= [0]*n  # will store the score of array till index 'i' i.e arr[....i]
                    # in Q :" score of an array arr as the sum of the values of the conversion array of arr."
        ans[0]= conver[0]
        for i in range(1, n):
            ans[i]= conver[i] + ans[i-1]
        return ans
    


# concise version of above

from itertools import accumulate
class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        maxTillNow, conver= 0, []  # min val of nums[i]= 1
        for n in nums:
            maxTillNow= max(maxTillNow, n)
            conver.append(n + maxTillNow)
        return accumulate(conver)  # convert the given array into prefix array original array will be same only.
                                   # with print you will have to also specify the type like "print(list(accumulate(conver)))" otherwise will give object address.
