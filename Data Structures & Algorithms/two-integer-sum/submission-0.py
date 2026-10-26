class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # If the complement is in the hash map, we found the pair!
            if complement in seen:
                return [seen[complement], i]
            
            # Otherwise, save the current number and its index to the map
            seen[num] = i
