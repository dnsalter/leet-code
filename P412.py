class Solution(object):
	def fizzBuzz(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		ar = []
		for i in range(1,n+1):
			if i%3 and i%5:
				ar.append(i)
			else:
				ar.append("Fizz"*bool(i%3)+"Buzz"*bool(i%5))
		return ar
			
if __name__ == '__main__':
	print(Solution().fizzBuzz(3))
