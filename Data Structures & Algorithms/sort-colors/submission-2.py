class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        """
        track leftmost position
        track rightmost position

        one pass through list
        if found 0, move to leftmost position
            swap 
        """
            
        i=0    
        low=0
        # mid=0
        high=len(nums)-1

        while i <= high:
            if nums[i]==0:
                nums[low], nums[i] = nums[i], nums[low]
                low+=1
                i+=1
            elif nums[i]==1:
                i+=1
            else:
                nums[high], nums[i] = nums[i], nums[high]
                high-=1



