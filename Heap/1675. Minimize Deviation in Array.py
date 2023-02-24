# Double odd numbers and put all numbers into a max heap. 
# i.e first convert all the number into even.
# Track the smallest number. Track the minimum difference between the top of the heap and the smallest number.
#  While the top of the heap is even, remove it, divide, and put back to the heap.
# vvi: reducing the maximum no till max number is even that's it.

# time: O(nlogn*)

# vvi: for odd number , we can perform only one operation i.e n*2 for one time since it will become 'even' after multiplying with '2'.
# on even number we can perform operation any number of time till it becomes odd.

# my dilemma: Where to stop? How to fugure out where to stop.
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        maxHeap= []   # creating maxHeap to get the maximum of the array in logn.
        minimum= float('inf')   # will keep track of minimum ele in the array at any point of time.
        # O(nlogn)
        for n in nums:
            if n % 2:  # if odd
                n= n*2   # making all odd to its maximum possible value it can take.
            minimum= min(minimum, n)
            heapq.heappush(maxHeap, -1*n)   # creating the maxHeap so pushing the negative value.

        difference= float('inf')    # will give the difference between minValue and maxValue at any point of time.
        # o(n*logn*logm)   # we have to make the highest number('m') to odd number so 'logm' i.e maximum variation of max number.
        while -1* maxHeap[0] % 2==0:   # while max ele is even. Reducing the max and max can be reduced to an odd number.
            maximum= -1* heapq.heappop(maxHeap)            
            difference= min(difference, maximum- minimum)
            minimum= min(minimum, maximum//2)
            heapq.heappush(maxHeap, -1* maximum//2)
        return min(difference, -1* maxHeap[0]- minimum)

