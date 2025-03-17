def revert_char(chars):
    test = [r for r in chars if r.isalpha()]
    print(test)

    temp = []

    for i in chars:
        if i.isalpha():
            temp.append(test.pop())
        else:
            temp.append(i)
    print(temp)
    merged_string = ''.join(temp)
    print(merged_string)

charr = 'Try Reverse String'
revert_char(charr)
