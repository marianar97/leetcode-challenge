# description:
# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Example 1:
# Input: s = "abciiidef", k = 3
# Output: 3

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = 'aeiou'
        max_vowels = 0
        cnt = 0 
        i, j = 0, 0
        while j < len(s):
            if (j - i  + 1) < k:
                if s[j] in vowels:
                    cnt += 1
                j += 1
            elif (j - i + 1) == k:
                if s[j] in vowels:
                    cnt += 1
                max_vowels = max(max_vowels, cnt)
                if s[i] in vowels:
                    cnt -= 1
                i += 1
                j += 1
                

                    
        return max_vowels