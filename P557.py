class Solution(object):
	def reverseWords(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		ar = s.split(" ")
		for i, word in enumerate(ar):
			ar[i] = word[::-1]
		return " ".join(ar)
		
if __name__ == '__main__':
	print(Solution().reverseWords("Let's take LeetCode contest"))