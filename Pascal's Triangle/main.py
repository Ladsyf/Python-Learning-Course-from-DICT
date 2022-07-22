# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def generate(numRows):
    pascal = []
    for x in range(numRows):
        indi = []
        for y in range(x+1):
            if y > 0 and y != x:
                indi.insert(y, pascal[x-1][y-1] + pascal[x-1][y])
            else:
                indi.insert(y, 1)

        pascal.insert(x, indi)

    return pascal

print(generate(6))




