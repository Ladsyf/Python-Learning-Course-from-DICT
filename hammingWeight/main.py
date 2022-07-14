# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def hammingWeight(self, n):
    n = bin(n)
    ans = 0
    for x in list(str(n)):
        if x == "1":
            ans = ans + 1
            print("plus 1")

    return ans
