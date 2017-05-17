def CommaCode(lst):
    commaCode = ''
    lst.insert(-1,'and')
    for i in range(len(lst)):
        if i == len(lst) - 1:
            commaCode += str(lst[i])
        elif i == len(lst) - 2:
            commaCode += str(lst[i]) + ' '
        else:
            commaCode += str(lst[i]) + ', '
    return commaCode

spam = [3, 'monkey', 1.56, True]
print(CommaCode(spam))
