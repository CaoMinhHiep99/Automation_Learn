def sort_string_custom(input_string):
    char_list = list(input_string)
    n = len(char_list)

    for i in range(n):
        for j in range(0, n - i - 1):
            if char_list[j].lower() > char_list[j + 1].lower():
                char_list[j], char_list[j + 1] = char_list[j + 1], char_list[j]
            elif char_list[j].lower() == char_list[j + 1].lower() and char_list[j] > char_list[j + 1]:
                char_list[j], char_list[j + 1] = char_list[j + 1], char_list[j]
    lower = []
    upper = []
    output = []
    for char in char_list:
        if char.isupper():
            upper.append(char)
        else:
            lower.append(char)
    for i in range(len(lower)):
        output.append(lower[i])
        output.append(upper[i])
    print(output)

    return ''.join(output)

if __name__ == "__main__":
    str = "DdAaCcbB"
    print(sort_string_custom(str))