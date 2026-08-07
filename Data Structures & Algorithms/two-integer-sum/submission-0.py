class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_map = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in number_map:
                return [number_map[diff], i]

            number_map[num] = i

        return []