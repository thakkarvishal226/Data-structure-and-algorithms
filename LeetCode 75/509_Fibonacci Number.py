class Solution:

    def __init__(self) -> None:
        self.count = 0
    memory_map = {}
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        if f'{n}' in self.memory_map.keys():
            return self.memory_map[f'{n}']
        else:
            self.memory_map[f'{n}'] = self.fib(n - 1) + self.fib(n - 2)
        return self.memory_map[f'{n}']




if __name__ == "__main__":
    s = Solution()
    print(s.fib(2))
    print(s.count)