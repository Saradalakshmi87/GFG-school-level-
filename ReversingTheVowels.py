class Solution:
    def modify(self, s):
        # code here
        toList = list(s)
        v = "aeiou"
        n = len(s)
        i, j = 0, n - 1
        while i < j:
            if (s[i] in v) and (s[j] not in v):
                j -= 1
            elif (s[i] not in v) and (s[j] in v):
                i += 1
            elif (s[i] not in v) and (s[j] not in v):
                i += 1
                j -= 1
            else:
                toList[i], toList[j] = toList[j], toList[i]
                i += 1
                j -= 1
        return ''.join(toList)

ob = Solution()
s = int(input())
print(ob.modify(s))