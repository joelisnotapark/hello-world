# first_last6
def first_last6(nums):
    if nums[0] == 6 or nums[len(nums) - 1] == 6:
        return True
    return False
    
    
# same_first_last
def same_first_last(nums):
    if (len(nums) > 0 and nums[0] == nums[len(nums) - 1]):
        return True
    return False
    
    
# common_end
def common_end(a, b):
    if a[len(a) - 1] == b[len(b) - 1] or a[0] == b[0]:
        return True
    return False
    
    
# sum3
def sum3(nums):
    return nums[0] + nums[1] + nums[2]
    
    
# rotate_left3
def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]
    
    
# reverse3
def reverse3(nums):
    return [nums[2], nums[1], nums[0]]
    
    
# sum2
def sum2(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    return nums[0] + nums[1]
    return sum(nums[0:2])


# middle-way
def middle_way(a, b):
    return [a[1], b[1]]
    
    
# make_ends
def make_ends(nums):
    return [nums[0], nums[len(nums) - 1]]
   
   
# has23
def has23(nums):
  if nums[0] == 2 or nums[0] == 3:
    return True
  if nums[1] == 2 or nums[1] == 3:
    return True
  return False  
