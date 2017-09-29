class Solution(object):
	def arrayPairSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		nums.sort()
		tot = 0
		for i in range(0,len(nums),2):
			tot += nums[i]
		return tot
		
if __name__ == '__main__':
	print(Solution().arrayPairSum([1,4,3,2]))