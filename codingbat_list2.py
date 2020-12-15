# count_evens
def count_evens(nums):
    count = 0
  
    for i in range(0, len(nums), 1):
        if (nums[i] % 2 == 0):
            count = count + 1
  
    return count
    
    
# big_diff
def big_diff(nums):
    maximum = nums[0]
    minimum = nums[0]

    for i in range(1,len(nums)):
        maximum = max(maximum, nums[i])
        minimum = min(minimum, nums[i])

    return maximum - minimum
    
    
# centered_average
def centered_average(nums):
    return (sum(nums) - max(nums) - min(nums)) / (len(nums) - 2)
    
   
# sum13
def sum13(nums):
    x = 0
    i = 0

    while i < len(nums):
        if nums[i] == 13:
            i += 1
        else:
            x += nums[i]
        i += 1

    return x
    
    
# sum67
def sum67(nums):
    sum = 0
    flag = False

    for i in range(len(nums)):
        if nums[i] == 6:
            flag = True
        if not flag:
            sum += nums[i]
        if nums[i] == 7 and flag:
            flag = False

    return sum
    
    
# has22
def has22(nums):
    for i in range(len(nums)-1):
        if nums[i] == 2 and nums[i+1] == 2:
            return True
                
    return False


# more_14
def more_14(nums:int) -> bool:
    pass
    i = 0
    x = 0
    y = 0
    while i < len(nums):
        if nums[i] == 1:
            x += 1
        elif nums[i] == 4:
            y += 1
        i += 1
        
    if x > y:
        return True
    else:
        return False

    
# lucky_13
def lucky_13(nums:int) -> bool:
    pass
    i = 0
    while i < len(nums):
        if nums[i] == 1:
            return False
        elif nums[i] == 3:
            return False
        i += 1
        
    return True


# sum_28
def sum_28(nums:int) -> bool:
    pass
    i = 0
    countoftwo = 0
    while i < len(nums):
        if nums[i] == 2:
            countoftwo += 1
        i += 1
    
    countoftwo = countoftwo * 2
    if countoftwo == 8:
        return True
    else:
        return False
    
    
# no_14
def no_14(nums:int) -> bool:
    pass
    i = 0
    valid = False
    while i < len(nums):
        if nums[i] != 1 and nums[i] != 4:
            valid = True
        else:
            valid = False
        i += 1
    return valid
