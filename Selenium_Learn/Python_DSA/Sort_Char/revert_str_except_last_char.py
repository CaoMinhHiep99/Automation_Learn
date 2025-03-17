def revert_str_except_last_char(chars):
    list_str = []
    temp = []
    for char in chars:
        list_str.append(char)
    last_element = list_str.pop()
    print(last_element)
    for i in range(len(list_str)):
        temp.append(list_str.pop())
    text = ''.join(temp)
    output = text + last_element
    print(output)
    return output

if __name__ == "__main__":
    str = "Automation"
    print(revert_str_except_last_char(str))