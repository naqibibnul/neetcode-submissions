class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        twos_moved = 0

        while i < len(nums) - twos_moved:
            if nums[i]==0:
                x = nums[i]
                del nums[i]
                nums.insert(0,x)
                i+=1
            elif nums[i] == 2:
                x = nums[i]
                del nums[i]
                nums.insert(len(nums),x)
                twos_moved+=1
            else:
                i+=1