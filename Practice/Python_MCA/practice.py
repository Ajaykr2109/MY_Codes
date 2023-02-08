# remove duplicates
class Solution:
    def removeDuplicates(self, input1):

        if input1 is None or len(input1) == 0:
            return ""
        # check input is string or not
        if not isinstance(input1, str):
            return None

        ans = ""
        for i in input1:
            if i not in ans:
                ans += i
        return ans


print(Solution().removeDuplicates("aabbccdd"))

# python 3.6
# remove duplicates
class solution:
    def removeduplicates(self, input1):
        # return "".join(set(input1))
        return "".join(dict.fromkeys(input1))


print(solution().removeduplicates("aabbccdd"))
