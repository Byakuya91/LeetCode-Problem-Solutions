class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        res = []
        letters = {'2':['a','b','c'] , '3':['d','e','f'] , '4':['g','h','i'] , '5':['j','k','l'] , '6':['m','n','o'] , '7':['p','q','r','s'] , '8':['t','u','v'], '9':['w','x','y','z']}

        def backTrack(temp,index):
            if len(temp) == n:
                return temp

            for j in letters[digits[index]]:
                temp += j
                a = backTrack(temp, index+1)
                if a:
                    res.append(a)
                temp = temp[0:-1]

        backTrack('',0)

        return res