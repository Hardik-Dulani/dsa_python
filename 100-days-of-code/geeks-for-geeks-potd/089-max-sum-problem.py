# Maximum Sum Problem
# EasyAccuracy: 57.09%Submissions: 38K+Points: 2
# Internship Alert!
# Become an SDE Intern by topping this monthly leaderboard! 

# banner
# A number n can be broken into three parts n/2, n/3, and n/4 (consider only the integer part). Each number obtained in this process can be divided further recursively. Find the maximum sum that can be obtained by summing up the divided parts together.
# Note: It is possible that we don't divide the number at all.

class Solution:
    def maxSum(self, n):
        memo = [-1] * (n + 1)

        def help(num):
            if num <= 1:
                return num

            if memo[num] != -1:
                return memo[num]
               
            part1 = help(num // 2)
            part2 = help(num // 3)
            part3 = help(num // 4)

            current_sum = part1 + part2 + part3

            memo[num] = max(current_sum, num)

            return memo[num]

        return help(n)


