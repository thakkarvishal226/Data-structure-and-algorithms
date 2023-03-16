class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_copy = ""
        t_copy = ""
        for i in range(len(s)):
            if s[i] == '#':
                s_copy = s_copy[:len(s_copy)-1]
            else:
                s_copy += s[i]
        for i in range(len(t)):
            if t[i] == '#':
                t_copy = t_copy[:len(t_copy)-1]
            else:
                t_copy += t[i]
        return s_copy == t_copy



if __name__ == "__main__":
    sol = Solution()
    s = "ab#c"
    t = "ad#c"
    print(sol.backspaceCompare(s, t))