class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        max_range = len(nums)
        numsdup = list(range(max_range + 1)) #array on numbers from 0 to n=(len(nums))

        result = list(set(nums) ^ set(numsdup))
        return result[0]