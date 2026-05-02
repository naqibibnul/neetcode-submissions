class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d = {}

        for _ in nums:
            if _ in d:
                d[_] += 1
            else:
                d[_] = 1

        print(d)

        out=[]
        

        while k>0:
            i,j = 0,0
            for key, value in d.items():
                if value > i:
                    i = value
                    j = key
                    print(j)
            k-=1    
            out.append(j)
            del d[j]

        print(len(d))
        print(out)

        return out

