# method 1: Recursive way
# same as fibonacii
# logic: just reverse the problem i.e reach to stair '1' from nth stair so no that we can do in same function
def frogJump(n: int, heights: List[int]) -> int:
    if n==1:  # means we have reached the destination so simply return '0'
        return 0
    if n==2: # only we have to go one step 
        return abs(heights[1] - heights[0])
    mn= 9999999
    mn= min(abs(heights[n-1]-heights[n-2]) + frogJump(n-1,heights),  abs(heights[n-1]-heights[n-3]) + frogJump(n-2,heights))
    return mn


# method 2: memoization (Top Down )
def frogJump(n: int, heights: List[int]) -> int:
    dp = [-1]*n
    return helper(n,heights,dp)

def helper(n,heights,dp):
    if n==1:  # means we have reached the destination so simply return '0'
        return 0
    if n==2: # only we have to go one step 
        return abs(heights[1] - heights[0])
    if dp[n-1]!= -1:
        return dp[n-1]
    dp[n-1]= 9999999  # as indexing is starting from 1
    dp[n-1]= min(abs(heights[n-1]-heights[n-2]) + helper(n-1,heights,dp),  abs(heights[n-1]-heights[n-3]) + helper(n-2,heights,dp))
    return dp[n-1]


# method 3: Tabulation bottom up
def frogJump(n: int, heights: List[int]) -> int:
    dp = [0]*n # at stair '0' energy lost= 0 
    dp[1]= abs(heights[1] - heights[0])  # height 2 to height 1
    for i in range(3,n+1): # from stair 3 to stair n
        dp[i-1]= min(abs(heights[i-1]-heights[i-2]) + dp[i-2],  abs(heights[i-1]-heights[i-3]) + dp[i-3])
    return dp[n-1]

# optimising space 
# same we did in fibonacii
