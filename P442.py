class Solution(object):
	def findDuplicates(self, nums):
		"""
		:type n: int
		:rtype: List[str]
		"""
		dic = {}
		ar = []
		for i in nums:
			if not(str(i) in dic):
				dic[str(i)] = 0
			dic[str(i)] += 1
		
		for i in dic:
			if dic[i] == 2:
				ar.append(int(i))
		
		return ar
			
if __name__ == '__main__':
	print(Solution().findDuplicates([4,3,2,7,8,2,3,1]))