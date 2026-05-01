class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        print(n)

        ans = []
        
        # for i in range(2*n+1):


        for i in range(2*n):
            ans.append(nums[i%n])
            print(i%n)
            # i++

        print(ans)

        return ans

