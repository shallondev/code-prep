# Run Time O(n^2)
class Solution:
    def twoSum(self, nums, target):
        
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i == j:
                    continue
                if num1 + num2 == target:
                    return [i, j]
       
        # If no solution found
        return None
    
# Run Time O(n)
class Solution:
    def twoSum(self, nums, target):
        
        # Define a hashmap
        hashmap = {}
        total_nums = len(nums)

        # Assign numbers to index
        for index in range(total_nums):
           hashmap[nums[index]] = index

        # Find two sum
        for index in range(total_nums):
            num = target - nums[index]

            # Check found two sum in hashmap and not ourselves
            if num in hashmap and hashmap[num] != index:
                return [index, hashmap[num]]