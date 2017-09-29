class Solution(object):
	def reverse(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		if int(str(abs(x))[::-1]) >= 2147483647:
			return 0
		elif x < 0:
			return -int(str(-x)[::-1])
		else:
			return int(str(x)[::-1])
			
if __name__ == '__main__':
	print(Solution().reverse(123))