# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

integer = int(4738964)

def comp(num):
    bin = ""
    complementnum = 0
    invisibleholder = 1
    while num != 0:
        bin = bin + str(int(not(bool(num % 2))))
        num = int(num / 2)
    for x in list(bin):
        if bool(int(x)):
            complementnum = complementnum + invisibleholder
        invisibleholder = invisibleholder*2

    return complementnum

print(comp(integer))
