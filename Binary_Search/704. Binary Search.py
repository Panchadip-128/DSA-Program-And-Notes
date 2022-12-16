# Note: in Binary search mid will give the ans always. so for making any decision or condition in 'if' or 'while' loop, just think from 'mid' 
# i.e if it is not equal to mid then where to move for this 'if' condition.

# Note: for initialising 'low' and 'up' just find the range in which we can get the ans.
# and initialise 'low'= min range value and 'up'= maximum range value.
# after this use template 1 or template 2 according to the Q.

# 'up' hmesha '>= target' me update hoga and low '<=' target me update hoga, kyonki hmlog ko size hmesha decrease karna h.

# Template 1:
# Note: use this template in case if elements are not present in and in case of not present also  we have to return some valid number, and
# if present simply then simply we will get the ans inside the while loop.
# e.g: Q like: 1) find ceil and floor of a number in sorted array  2) find square root of a number  
# 3) Find 1st bad version 4) 744. Find Smallest Letter Greater Than Target 5) 35. Search Insert Position

# here while loop will only break when low>up then 'low' will give the ceil value(just greater than key) and 
# 'high' will give the floor value(just less than key) since after while loop low will become '1' greater than 'high'.

# in case of duplicate ele it will give any index where it will find the ans first.
def binary_search(arr,key):
    n= len(arr)
    low=0
    up= n-1
    while(low<= up):
        mid= low+ (up-low)//2
        if arr[mid]== key:
            return mid
        elif(arr[mid]> key):  # mid ans deta but mid hi bda h to ab kahan 'key' hmko mil sakta h. mid se phle
            up= mid-1
        elif(arr[mid]<key):
            low= mid+1
    return -1

# arr= [10, 20, 30, 50, 60, 80, 110, 130, 140, 170]
# key= 1
# print(binary_search(arr, key))


# another way:
# here after while loop will break then 'low' and 'high' will become equal.
# so any one of them will point to 'key' if key is present.

# Template 2: 
# use this template when we are asked to return ans if present else simply return '-1'
# (or something fixed value given to return in case if not present) or given ans exist for sure.
# here we make decision after while loop only. 
# e.g: search for an element in an array.

# in case of duplicate elements, it will give the 1st index where ele is present.
# because even after finding the ans(>=), we are continuing our checking and shrinking the mid(decreasing the up).

# agar ans mil bhi gya ho(>=) to or range shrink karke(up ko decr karke) even or chota dhundho.
def binary_search(arr,key):
    n= len(arr)
    low=0
    up= n-1
    while low< up:
        mid= low+ (up-low)//2
        if(arr[mid]>= key):    
            up= mid         # agar hmko target ele hi find karna h kisi smaller index pe then do this
        else:
            low= mid+1
    return low if arr[low]== key else -1
    
arr= [10, 10,20, 30, 50, 60, 80, 110, 110, 130, 140, 170]
key= 10
print(binary_search(arr, key))


# Note: every binary search problem can be solved using these two(1 and 2) template with exact one or with slight modification 
# in while loop condidtion or in 'if' condition or both.
# after each Q, find out which template we can use and what modification we have to make acc to the Q.


# another way
# here after while loop will break then 'low' and 'high' will become equal.
# so any one of them will point to 'key' if key is present.

# Template 3:  same as Template 2

# in case of duplicate elements, it will give the last index where ele is present.
# because even after finding the ans, we are continuing our checking and increasing the mid(increasing the low).
# but doesn't work always to get the last index. may get TLE also . e.g" [10,10], key= 10
# so avoid this template to find the last index. 

def binary_search(arr,key):
    n= len(arr)
    low=0
    up= n-1
    while low< up:
        mid= low+ (up-low)//2
        if(arr[mid] <= key):    
            low= mid
        else:
            up= mid-1
    return up if arr[up]== key else -1
    
arr= [10, 10,20, 30, 50, 60, 80, 110, 110, 130, 140, 170]
key= 10
# print(binary_search(arr, key))


# to find the last index. basic one.
# template 1 only 
def binary_search(nums,target):
    ans= -1
    start= 0
    end= len(nums)-1
    while start<= end:
        mid= start+ (end-start)//2
        # updaet ans and incr the start
        if nums[mid]== target:
            ans= mid  
            start= mid+1  # for finding larger index. means we have to find beyond mid
        elif nums[mid]> target:
            end= mid-1
        else:
            start= mid+1
    return ans

arr= [10, 10,20,20,20,20]
key= 20
print(binary_search(arr, key))


# another concise way of above method(merge two if into one if)
# template 1 only
def binary_search(nums,target):
    start= 0
    end= len(nums)-1
    while start<= end:
        mid= start+ (end-start)//2
        if nums[mid]<= target:
            start= mid+1  # for finding larger index. means we have to find beyond mid
        else:
            end= mid-1
    # after while loop, end will point to the last index of target
    # (as before while loop exit start had last index value since equal to(<=) condition with 'start') and
    # 'start' will point to the smallest greater ele than the target
    return end  

arr= [10, 10, 10,10,20,20,20,20,20]
key= 10
print(binary_search(arr, key))

# Q: To find the 1st index of any target element
def binary_search(arr,key):
    n= len(arr)
    low=0
    up= n-1
    while low<= up:
        mid= low+ (up-low)//2
        if(arr[mid]>= key):    
            up= mid-1        # agar hmko target ele hi find karna h kisi smaller index pe then do this
        else:
            low= mid+1
    # after while loop, low will point to the 1st index as before while loop exit 'up' was pointing 
    # to the required ans(due to '>=' condition with up).
    # 'up' will point to the greatest number smaller than the target.
    return low
