#Given a string, find the length of the longest substring without repeating characters.
#
#Examples:
#
#Given "abcabcbb", the answer is "abc", which the length is 3.
#
#Given "bbbbb", the answer is "b", with the length of 1.
#
#Given "pwwkew", the answer is "wke", with the length of 3. 
#Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
	def lengthOfLongestSubstring(self, s):
		uniqueSub = []
		uniqueStr = ""
		
		if len(s) <= 1:
			return len(s)
		
		for i in range(len(s)-1):
			uniqueStr = ""
			
			for j in s[i:]:
				if j not in uniqueStr:
					uniqueStr+=j
				else:
					break
			uniqueSub.append(uniqueStr)
			
		uniqueStr = ""
		
		for i in uniqueSub:
			if len(i) > len(uniqueStr):
				uniqueStr = i
				
		return len(uniqueStr)
		
if __name__ == '__main__':
	print(Solution().lengthOfLongestSubstring("pwwkew"))
