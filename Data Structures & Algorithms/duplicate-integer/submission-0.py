class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hset = set()
        for idx in nums:
            if idx in hset:
                return True
            hset.add(idx)
        return False