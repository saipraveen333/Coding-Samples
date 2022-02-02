class Solution:
	def combine(self,n, k):
		nums = [i for i in range(1, n + 1)]
		res = []
		def helper(tmp, nums):
			if len(tmp) == k:
				res.append(tmp)
				return
			for i in range(len(nums)):
				helper(tmp + [nums[i]], nums[i + 1:])
		helper([], nums)
		return res
s=Solution()
print(s.combine(5,2))



