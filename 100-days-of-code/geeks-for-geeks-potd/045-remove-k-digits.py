# Remove K Digits
# MediumAccuracy: 26.8%


# Given a non-negative integer S represented as a string, remove K digits from the number so that the new number is the smallest possible.
# Note : The given num does not contain any leading zero.


class Solution:

    def removeKdigits(self, S, K):
        # code here
        length = len(S)
        if K == length:
            return "0"

        result = []
        i = 0
        while i < length:
            while K > 0 and result and result[-1] > S[i]:
                result.pop()
                K -= 1
            result.append(S[i])
            i += 1

        while K > 0:
            result.pop()
            K -= 1

        ptr = 0
        while ptr < len(result) and result[ptr] == '0':
            ptr += 1

        result = result[ptr:]
        return "0" if not result else "".join(result)
