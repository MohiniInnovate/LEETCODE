class Solution:
    def kthCharacter(self, k: int) -> str:


        def game(s):
            new_s = ''

            for c in s:
                new_s += chr(ord(c) + 1)

            s += new_s

            if len(s) >= k:
                return s[k-1]

            return game(s)

        return game('a')
        




        