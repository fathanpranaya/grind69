class Solution:
    def isPalindrome(self, s: str) -> bool:
        # cleanup string
        s_clean = ''.join(ch for ch in s if ch.isalnum()).lower()

        right = len(s_clean) - 1
        left = 0
        while left < right:
            if s_clean[right] != s_clean[left]:
                return False

            right -= 1
            left += 1
            
        return True

if __name__ == "__main__":
    s = Solution()
    i = "race a car"
    print(s.isPalindrome(i))