class Solution:    

    # ["Hello", "World"] -> "HelloWorld"
    def encode(self, strs: List[str]) -> str:
        res = [] # faster than res = ""
        for c in strs:
            res.append(str(len(c)) + '#' + c)
        return ''.join(res)

    # "5#Hello5#World" -> ["Hello", "World"]
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length

        return res
       