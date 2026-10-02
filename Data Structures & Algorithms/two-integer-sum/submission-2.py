class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {value: i for i, value in enumerate(nums)}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in hashmap and hashmap[dif] != i:
                return [i, hashmap[dif]]