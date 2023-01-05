
def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
    nums.sort()
    prev = [-1] * len(nums)
    V = [1] * len(nums)
    for i in range(1,len(nums)):
        prev[i] = max(filter(lambda jdx: nums[i] % nums[jdx] == 0, range(i)), key=lambda jdx: V[jdx],default=-1)
        V[i] += V[prev[i]]
    
    tNode = max(range(len(nums)), key=lambda num: V[num])
    
    ret = []
    while tNode != -1:
        ret.append(nums[tNode])
        tNode = prev[tNode]
    return ret        