class Solution(object):
    def matrixReshape(self, mat, r, c):
        row=len(mat)
        col=len(mat[0])
        if row * col!=r*c:
            return mat
        nums=[]
        for i in mat:
            nums.extend(i)
        ans = []
        for i in range(0, len(nums), c):
            ans.append(nums[i:i + c])
        return ans

        