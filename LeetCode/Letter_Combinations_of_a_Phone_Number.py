# DFS + Backtracking
# DFS에서 인자 넘길때 유의

from collections import defaultdict

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []

        d = defaultdict(str)

        alphabet = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        # defaultdict(<class 'str'>, {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'})

        for i in range(2, 10):
            d[i] = alphabet[i-2]

        print(d)

        digits_list = []
        # [2, 3]
        for i in digits:
            digits_list.append(int(i))

        print(digits_list)

        result = []

        def backtracking(i, string, depth):
            if depth == len(digits):
                result.append(string)
                return

            for s in d[digits_list[i]]:
                # print(s)
                # string = ""
                # string += s
                # backtracking(i+1, string, depth+1)
                backtracking(i+1, string + s, depth+1)
            # print()

        backtracking(0, "", 0)

        print(result)

        return result
