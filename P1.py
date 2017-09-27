# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution(object):
	def twoSum(self, nums, target):
		for i in range(len(nums)-1):
			for j in range(len(nums)-1):
				if (nums[i] + nums[j]) == target:
					return [i,j]
		
if __name__ == '__main__':
	print(Solution().twoSum((2, 7, 11, 15), 9))