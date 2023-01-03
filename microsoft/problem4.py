
def maxRotateFunction( A):
    s, n = sum(A), len(A)
    cur_sum = sum([i*j for i, j in enumerate(A)])
    ans = cur_sum
    for i in range(n): ans = max(ans, cur_sum := cur_sum + s-A[n-1-i]*n)
    return ans
A=[1,2,3,4]
print(maxRotateFunction(A))