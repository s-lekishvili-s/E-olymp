num = input()
length = len(num)
if num == '9' * length:
    print(length + 1)
else:
    print(length)