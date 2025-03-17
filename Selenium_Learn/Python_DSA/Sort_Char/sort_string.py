def sort_string(input_string):

    char_list = list(input_string)

    n = len(char_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if char_list[j] > char_list[j + 1]:
                char_list[j], char_list[j + 1] = char_list[j + 1], char_list[j]

    return ''.join(char_list)

if __name__ == "__main__":
    str = "ICON"
    print(sort_string(str))