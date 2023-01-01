class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        if k>n:
            return []
        if n>45:
            return []


        ans=[]

        lst=range(1,10)
     


        def solver(ind, output, target):

            if len(output)==k and target==0:

                ans.append(output[:])
                return 
            
            for i in range(ind, len(lst)):

                if target < lst[i]:
                    break

                output.append(lst[i])
                solver(i+1, output, target-lst[i])
                output.pop()
        solver(0, [], n)

        return ans

            

       