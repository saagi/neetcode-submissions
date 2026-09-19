import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        clean_text = re.sub(r'[^a-zA-Z0-9]', '', s)
        return clean_text==clean_text[::-1]
        