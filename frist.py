# (4)
def ceil(num):
    if num < 0:
        return int(num)
    else:
        if num - int(num) == 0:
            return num
        else:
            return int(num) + 1
print(ceil(3.5))
print(ceil(4))
print(ceil(-1.2))
print(ceil(-1))
