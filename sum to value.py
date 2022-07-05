class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [hashmap[complement], i]
            hashmap[nums[i]] = i

Sumtovalue = Solution()
print(Sumtovalue.twoSum(nums = [5, 8, 1, 14, 4, 8, 7, 3], target = 5))