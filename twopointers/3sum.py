  
def threesum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        # Skip duplicates for i
        if i > 0 and nums[i] == nums[i-1]:
            continue
            
        tar = nums[i] 
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            current_sum = nums[left] + nums[right] + tar
            
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for left
                if  left < right and nums[left] == nums[left+1]:
                    left += 1
                # Skip duplicates for right
                if  left < right and nums[right] == nums[right-1]:
                    right -= 1
                    
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    
    return result


arr = [-1,0,1,2,-1,-4]
nums = [2,-2,0,0]
print(threesum(arr))  # Should print: [[-1,-1,2], [-1,0,1]]
print(threesum(nums)) # Should print: [[-2,0,2], [0,0,0]]