class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # brute force
        s_clean = "".join(char for char in s if char.isalnum()).lower()
        s_reverse = s_clean[::-1]

        return True if s_clean == s_reverse else False