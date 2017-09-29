class Solution(object):
	def fizzBuzz(self, n):
		"""
		:type n: int
		:rtype: List[str]
		"""
		ar = []
        for i in range(1,n+1):
            ar.append("")
            if not i % 3:
                ar[i-1] += "Fizz"
                if not i % 5:
                    ar[i-1] += "Buzz"
            elif not i % 5:
                    ar[i-1] += "Buzz"
            else:
                ar[i-1] = str(i)
        return ar
		
if __name__ == '__main__':
	print(Solution().fizzBuzz(3))