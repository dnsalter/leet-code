class Solution(object):
	def findComplement(self, num):
		"""
		:type num: int
		:rtype: int
		"""
		binNum = (str(bin(num))[2:])
		compNum = ""
		for ch in binNum:
			if ch == '1':
				compNum += '0'
			else:
				compNum += '1'
		return int(compNum,2)
		
if __name__ == '__main__':
	print(Solution().findComplement(5))