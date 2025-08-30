def two_sum(nums, target):
    """
    Find two numbers in the list that add up to the target.
    :param nums: List of integers
    :param target: Target sum
    :return: Tuple of indices of the two numbers that add up to the target
    """
    map = {}
    
    for index, num in enumerate(nums):
        complement = target - num
        if complement in map:
            return (map[complement], index)
        map[num] = index
    
    return None           # If no solution is found

sam= [2, 7, 11, 15]
target = 9
res = two_sum(sam, target)
print(res)                # Output should be (0, 1) since nums[0] + nums[1] == 9
                          # If no solution is found, it will return None