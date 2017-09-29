class Solution(object):
	def findWords(self, words):
		"""
		:type words: List[str]
		:rtype: List[str]
		"""
		rows = ["QWERTYUIOP", "ASDFGHJKL", "ZXCXVBNM"]
		acceptable = []
		flag = 0
		for word in words:
			for row in rows:
				for ch in word:
					if ch.upper() not in row:
						flag += 1
						break
			if flag < 3:
				acceptable.append(word)
			flag = 0
		return acceptable
		
if __name__ == '__main__':
	print(Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]))