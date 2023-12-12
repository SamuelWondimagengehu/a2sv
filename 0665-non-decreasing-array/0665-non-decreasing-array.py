class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        violation_counts = 0
        
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if violation_counts == 1:
                    return False
                violation_counts += 1

                if i >= 2 and nums[i - 2] > nums[i]:
                    nums[i] = nums[i - 1]
        
        return True
        