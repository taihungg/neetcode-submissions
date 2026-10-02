class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, value in enumerate(nums):
            dif = target - value
            if dif in hashmap:
                return [hashmap[dif], i]
            hashmap[value] = i