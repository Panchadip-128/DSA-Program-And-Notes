# method 1: Recursive Approach
# correct only but showing time limit exceeded
# just same as 0/1 knapsack except when you include that item
class Solution:
    def knapSack(self, N, W, val, wt):
        profit= 0
        if N==0 or W==0:
            return 0
        if wt[N-1]<= W:
            tempAns= max(val[N-1]+ self.knapSack(N,W- wt[N-1],val,wt), self.knapSack(N-1,W,val, wt))
            profit+= tempAns
        else:
            tempAns= self.knapSack(N-1,W,val, wt)
            profit+= tempAns
        return profit


# method2: By memoization
# corect only but two test cases not passing, have to see later
class Solution:
    def knapSack(self, N, W, val, wt):
        dp=[[-1 for j in range(W + 1)] for i in range(N +1)]  # initialising the answer matrix  
        return self.helper(N,W,val,wt,dp)
    def helper(self,N,W,val,wt,dp):
        if N==0 or W==0:
            return 0
        if dp[N][W]!= -1:
            return dp[N][W]
        if wt[N-1]<= W:
            dp[N][W]= max(val[N-1]+ self.helper(N,W- wt[N-1],val,wt,dp), self.helper(N-1,W,val, wt,dp))
        else:
            dp[N][W]= self.helper(N-1,W,val, wt,dp)
        return dp[N][W]


# method 3: Top Down Approach
class Solution:
    def knapSack(self, N, W, val, wt):
        dp= [[0 for i in range(W+1)] for i in range(N+1)]
        for i in range(1,N+1):
            for j in range(1,W+1):
                if wt[i-1]<= j:
                    dp[i][j]= max(val[i-1]+ dp[i][j-wt[i-1]], dp[i-1][j])
                else:
                    dp[i][j]= dp[i-1][j]
        return dp[N][W]

# method 4: space optimising to O(n)
