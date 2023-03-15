class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_mapping = {}
        guess_mapping = {}
        bulls = 0
        cows = 0
        for index in range(len(secret)):
            if secret[index] == guess[index]:
                bulls += 1
            else:
                secret_mapping[f"{secret[index]}"] = secret_mapping.get(f"{secret[index]}",0) + 1
                guess_mapping[f"{guess[index]}"] = guess_mapping.get(f"{guess[index]}",0) + 1
                if (secret_mapping.get(f"{secret[index]}",0) + guess_mapping.get(f"{secret[index]}",0)) == 2:
                    cows+=1
                    secret_mapping[f"{secret[index]}"] -= 1
                    guess_mapping[f"{secret[index]}"] -= 1

                if (guess_mapping.get(f"{guess[index]}",0) + secret_mapping.get(f"{guess[index]}",0)) == 2:
                    cows+=1
                    secret_mapping[f"{guess[index]}"] -= 1
                    guess_mapping[f"{guess[index]}"] -= 1

        return f"{bulls}A{cows}B"


if __name__ == "__main__":
    s = Solution()
    secret = "1234"
    guess = "0111"
    print(s.getHint(secret, guess))