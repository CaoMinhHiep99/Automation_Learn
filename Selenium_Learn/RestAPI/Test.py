# def reverse_words(str):
#     stack = []
#     word = ""

#     # Iterate through the string
#     for ch in str:
        
#         # If not a dot, build the current word
#         if ch != '.':
#             word += ch
        
#         # If we see a dot, push the word into the stack
#         elif word:
#             stack.append(word)
#             word = ""

#     # Last word remaining, push it to stack
#     if word:
#         stack.append(word)

#     # Rebuild the string from the stack
#     return ".".join(stack[::-1])

# if __name__ == "__main__":
#     str = "..geeks..for.geeks."
#     print(reverse_words(str))



# def sort_char(chars):
#     str = []
#     num = []

#     for char in chars:
#         if char.isalpha():
#             str.append(char)
#         else:
#             num.append(char)

#     print(f'str: {str}, num:{num}')

#     str = ''.join(str)
#     num = ''.join(num)

#     output = f'{str}{num}'
#     print(f'output:{output}')
#     return output

# if __name__ == "__main__":
#     str = "A1B2C3"
#     print(sort_char(str))


# def sort_string_upper_lower(chars):
#     lower = []
#     upper = []
#     output = []

#     for char in chars:
#         if char.isupper():
#             upper.append(char)
#         else:
#             lower.append(char)
#     lower = sorted(lower)
#     upper = sorted(upper)

#     print(f'lower: {lower}')
#     print(f'upper: {upper}')
#     char_num = len(lower)
#     for i in range(char_num):
#         output.append(lower[i])
#         output.append(upper[i])

#     print(lower)
#     return output



# if __name__ == "__main__":
#     str = "DdAaCcbB"
#     print(sort_string_upper_lower(str))



# def revert_str_except_last_char(chars):
#     list_str = []
#     temp = []
#     for char in chars:
#         list_str.append(char)
#     last_element = list_str.pop()
#     print(last_element)
#     for i in range(len(list_str)):
#         temp.append(list_str.pop())
#     text = ''.join(temp)
#     output = text + last_element
#     print(output)
#     return output

# if __name__ == "__main__":
#     str = "Automation"
#     print(revert_str_except_last_char(str))



# def test_sort(chars):
#     char = sorted(chars)
#     output = "".join(char)
#     print(output)
#     return output

# if __name__ == "__main__":
#     str = "ICON"
#     print(test_sort(str))


# def sort_string(input_string):

#     char_list = list(input_string)

#     n = len(char_list)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             # So sánh các ký tự và hoán đổi nếu cần
#             if char_list[j] > char_list[j + 1]:
#                 char_list[j], char_list[j + 1] = char_list[j + 1], char_list[j]

#     return ''.join(char_list)

# if __name__ == "__main__":
#     str = "ICON"
#     print(sort_string(str))


# def sort_string_custom(input_string):
#     char_list = list(input_string)
#     n = len(char_list)

#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if char_list[j].lower() > char_list[j + 1].lower():
#                 char_list[j], char_list[j + 1] = char_list[j + 1], char_list[j]
#             elif char_list[j].lower() == char_list[j + 1].lower() and char_list[j] > char_list[j + 1]:
#                 char_list[j], char_list[j + 1] = char_list[j + 1], char_list[j]
#     lower = []
#     upper = []
#     output = []
#     for char in char_list:
#         if char.isupper():
#             upper.append(char)
#         else:
#             lower.append(char)
#     for i in range(len(lower)):
#         output.append(lower[i])
#         output.append(upper[i])
#     print(output)

#     return ''.join(output)

# if __name__ == "__main__":
#     str = "DdAaCcbB"
#     print(sort_string_custom(str))



# def split_string(chars):
#     output = chars.split()[-1]
#     print(output)

# if __name__ == "__main__":
#     str = "I'm from USA"
#     print(split_string(str))


def bubble_sort(arr):
    for i in range(len(arr)):
        swap = False
        for j in range(0, len(arr) - i -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        if not swap:
            break
    print(arr)
    return arr


if __name__ == '__main__':
    array = [64, 34, 25, 12, 22, 11, 90]
    arr = bubble_sort(array)
    print(f'Array after sort: {arr}')