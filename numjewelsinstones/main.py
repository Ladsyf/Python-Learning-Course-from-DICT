# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def numJewelsInStones(self, jewels, stones):

    answer = 0
    for x in list(jewels):
        for y in list(stones):
            if (x == y):
                answer = 1 + answer
    return answer

jewels = ""
stones = ""
input(jewels)
input(stones)
print(numJewelsInStones(jewels, stones))

# rpoblem link: https://leetcode.com/problems/jewels-and-stones/
