import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count =  {}
        for i in s:
            if i in char_count.keys():
                char_count[f'{i}'] += 1 
            else:
                char_count[f'{i}'] = 1
        print(char_count)
        max_count = 0
        for i in char_count.values():
            
            max_count += i // 2 * 2
            print(max_count)
        return  min(max_count+1, len(s))

if __name__ == "__main__":
    s = Solution()
    input_string = "aaabaaaaliugeigaewfouyaergglhavrfg"
    print(s.longestPalindrome(input_string))
    print(s.longest2(input_string))
