# def bubble_sort(arr):
#     n = len(arr)
#     # Lặp qua toàn bộ mảng
#     for i in range(n):
#         # Biến kiểm tra để phát hiện nếu không có hoán đổi nào trong lần lặp này
#         swapped = False
#         # Lặp qua mảng từ đầu đến phần tử chưa được sắp xếp cuối cùng
#         for j in range(0, n - i - 1):
#             # So sánh và hoán đổi nếu cần thiết
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 swapped = True
#         # Nếu không có hoán đổi nào xảy ra, dừng vòng lặp
#         if not swapped:
#             break
#     return arr


# if __name__ == '__main__':
#     array = [64, 34, 25, 12, 22, 11, 90]
#     arr = bubble_sort(array)
#     print(f'Array after sort: {arr}')


# list1 = ['Hiep', 'name']
# list2 = ['My', 'is']


# mapping = {
#     1:list2[0],
#     2:list1[1],
#     3:list2[1],
#     4:list1[0]
# }
# sample_list = []
# for key, value in mapping.items():
#     sample_list.append(value)
# sample_str = ' '.join(sample_list)
# print(sample_str)

# list1 = [1,2,3]
# list2 = ['a','b','c']

# dict_sample = {}

# for key in list1:
#     for value in list2:
#         dict_sample[key] = value
#         list2.remove(value)
#         break
# print(f'{dict_sample}\n')


# def bubble_sort(arr):

#     num_arr = len(arr)
#     for i in range(num_arr - 1):
#         for j in range(num_arr - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr

# if __name__ == '__main__':
#     array = [64, 34, 25, 12, 22, 11, 90]
#     arr = bubble_sort(array)
#     print(f'Array after sort: {arr}')

# def bubble_sort(charr):
#     """
#     """
#     charr_list = list(charr)
#     num_charr = len(charr_list)
#     for i in range(num_charr - 1):
#         for j in range(num_charr - i - 1):
#             if charr_list[j].lower() > charr_list[j + 1].lower():
#                 charr_list[j], charr_list[j + 1] = charr_list[j + 1], charr_list[j]
#             elif charr_list[j].lower() == charr_list[j + 1].lower() and charr_list[j] > charr_list[j + 1]:
#                 charr_list[j], charr_list[j + 1] = charr_list[j + 1], charr_list[j]
#     return charr_list


# if __name__ == '__main__':
#     str_text = 'DdAaCcbB'
#     str_text = bubble_sort(str_text)
#     print(f'String after sort: {str_text}')

# def bubble_sort(charr):
#     """
#     """
#     charr_list = list(charr)
#     num_charr = len(charr_list)
#     for i in range(num_charr - 1):
#         for j in range(num_charr - i - 1):
#             if charr_list[j] > charr_list[j + 1]:
#                 charr_list[j], charr_list[j + 1] = charr_list[j + 1], charr_list[j]
#     return charr_list

# if __name__ == '__main__':
#     str_text = 'DdAaCcbB'
#     str_text = bubble_sort(str_text)
#     print(f'String after sort: {str_text}')


# def count_duplicate(sample_list):
#     """
#     """
    
#     str_test = ''.join(sample_list).lower()
#     duplicate = []
#     for i in str_test:
#         if str_test.count(i) > 1 and i not in duplicate:
#             duplicate.append(i)
#     return duplicate



# if __name__ == '__main__':
#     sample_list = ['My', 'country', 'is', 'Vietnamyyyyy']
#     sample_list = count_duplicate(sample_list)
#     print(f'String after sort: {sample_list}')

# if __name__ == '__main__':
#     thickness = int(input()) #This must be an odd number
#     c = 'H'
#     for i in range(thickness):
#         print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#     for i in range(thickness+1):  print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#     for i in range((thickness+1)//2):
#         print((c*thickness*5).center(thickness*6))    

#     for i in range(thickness+1): print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#     for i in range(thickness):  print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))



# import textwrap

# def wrap(samp_string, max_width):
#     temp_list = []
#     num_str = len(samp_string)
#     samp_list = list(samp_string)
#     range_num = num_str//max_width
#     if num_str % max_width != 0:
#         range_num = range_num + 1
#     for i in range(range_num):
#         temp_list.append(''.join(samp_list[:max_width]))
#         for j in samp_list[:max_width]:
#             samp_list.remove(j)
#     return '\n'.join(temp_list)

# def wrap(samp_string, max_width):
#     result = []
#     for i in range(0, len(samp_string)-1, max_width):
#         result.append(''.join(samp_string[i:i+max_width]))
#     return '\n'.join(result)

# if __name__ == '__main__':
#     # string, max_width = input(), int(input())
#     samp_string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
#     max_width = 5
#     result = wrap(samp_string, max_width)
#     print(result)


# def calculate_cakes(recipe, available):
#     # Khởi tạo số lượng bánh tối đa có thể làm từ mỗi nguyên liệu là vô cùng lớn
#     max_cakes = float('inf')
    
#     # Duyệt qua từng nguyên liệu trong công thức
#     for ingredient, amount_needed in recipe.items():
#         # Kiểm tra xem nguyên liệu có trong available hay không
#         if ingredient not in available:
#             return 0  # Nếu thiếu nguyên liệu thì không thể làm bánh
    
#         # Tính số lượng bánh có thể làm từ nguyên liệu này
#         max_cakes_from_ingredient = available[ingredient] // amount_needed
        
#         # Cập nhật số lượng bánh tối đa có thể làm được
#         max_cakes = min(max_cakes, max_cakes_from_ingredient)
    
#     return max_cakes

# # Ví dụ sử dụng
# recipe_1 = {'flour': 500, 'sugar': 200, 'egg': 1}
# available_1 = {'flour': 1200, 'sugar': 1000, 'egg': 5, 'oil': 5}
# max_cakes = calculate_cakes(recipe_1, available_1)  # Kết quả: 2
# print(f'\nmax_cakes = {max_cakes}')

# recipe_2 = {'flour': 1000, 'sugar': 200, 'egg': 1, 'butter': 500, 'oil': 1}
# available_2 = {'flour': 900, 'sugar': 1000, 'egg': 5}
# print(calculate_cakes(recipe_2, available_2))  # Kết quả: 0

# def bubble_sort(arr):
#     """
#     """
#     num_arr = len(arr)
#     for i in range(num_arr - 1):
#         for j in range(num_arr - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr

# if __name__ == '__main__':
#     array = [64, 34, 25, 12, 22, 11, 90]
#     arr = bubble_sort(array)
#     print(f'Array after sort: {arr}')

# def check_score(arr, n):
#     """
#     """
#     arr = list(arr)
#     for i in range(n - 1):
#         for j in range(n - i - 1):
#             if arr[j] < arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     for i in range(n):
#         if arr[i] == arr[0]:
#             continue
#         elif arr[i] < arr[0]:
#             return arr[i]



# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     exp = check_score(arr, n)
#     print(exp)


# def check_lowest(dict_score):
#     """
#     """
#     score_list = []
#     for value in dict_score.values():
#         score_list.append(value)
#     num_list = len(score_list)
#     for i in range(num_list - 1):
#         for j in range(num_list - i - 1):
#             if score_list[j] > score_list[j + 1]:
#                 score_list[j], score_list[j + 1] = score_list[j + 1], score_list[j]
#     for i in range(num_list):
#         if score_list[i] > score_list[0]:
#             second_low = score_list[i]
#             break
#     student_low = []
#     for key, value in dict_score.items():
#         if value == second_low:
#             student_low.append(key)
#     student_low = sorted(student_low)
#     for i in student_low:
#         print(i)


# if __name__ == '__main__':
#     dict_score = {}
#     for i in range(int(input())):
#         name = input()
#         score = float(input())
#         dict_score.update({name: score})
#     check_lowest(dict_score)

# def average_mark(student_marks, query_name):
#     """
#     """
#     for key, value in student_marks.items():
#         if key == query_name:
#             marks = 0
#             for i in value:
#                 marks = i + marks
#             aver_mark = marks/3
#             return aver_mark

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     aver_mark = average_mark(student_marks, query_name)
#     print("%.2f" %aver_mark)



# if __name__ == '__main__':
#     x = int(input()) + 1
#     y = int(input()) + 1
#     z = int(input()) + 1
#     n = int(input())
#     lst = []
#     for i in range(0,x):
#         for j in range(0,y):
#             for o in range(0, z): 
#                 if (i + j + o) != n: 
#                     lst.append([i,j,o])
#     print(lst)

# import argparse
# import json

# def test_dict(dic, li):
#     """
#     In ra dictionary và list
#     """
#     print("Dictionary:", dic)
#     print("List:", li)

# if __name__ == '__main__':
#     # Tạo đối số cho argparse
#     parser = argparse.ArgumentParser()

#     # Đối số đầu tiên: work_queue_input là chuỗi JSON cho dictionary
#     parser.add_argument('work_queue_input', type=str, help="Input work queue (JSON format)")

#     # Đối số thứ hai: doc_type_list là chuỗi cho list
#     parser.add_argument('doc_type_list', type=str, help="Input list of document types")

#     # Phân tích cú pháp các đối số từ command line
#     args = parser.parse_args()

#     # Chuyển đổi chuỗi JSON thành dictionary
#     n = json.loads(args.work_queue_input)

#     # Chuyển đổi chuỗi list thành list
#     m = json.loads(args.doc_type_list)

#     # Gọi hàm test_dict với dictionary và list đã phân tích
#     test_dict(n, m)

# def split_and_join(line: str):
#     line = line.split()
#     line = '-'.join(line)
#     return line

# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)

# def mutate_string(string: str, position: int, character: str):
#     l = list(string)
#     l = l[:position] + [character] + l[position + 1:]
#     string = ''.join(l)
#     return string

# if __name__ == '__main__':
#     s = input()
#     i = input()
#     c = input()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)

# def count_substring(string, sub_string):
#     exp_result = 0
#     for i in range(len(string)):
#         if string[i:len(sub_string) + i] == sub_string:
#             exp_result += 1
#         elif len(string[i:len(sub_string) + i]) < len(sub_string):
#             break
#     return exp_result


# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#     count = count_substring(string, sub_string)
#     print(count)

# if __name__ == '__main__':
#     s = input()
#     expect_result = []

#     r = 'False'
#     for i in list(s):
#         if i.isalnum():
#             r = 'True'
#             break
#     expect_result.append(r)

#     r = 'False'
#     for i in list(s):
#         if i.isalpha():
#             r = 'True'
#             break
#     expect_result.append(r)

#     r = 'False'
#     for i in list(s):
#         if i.isdigit():
#             r = 'True'
#             break
#     expect_result.append(r)

#     r = 'False'
#     for i in list(s):
#         if i.islower():
#             r = 'True'
#             break
#     expect_result.append(r)

#     r = 'False'
#     for i in list(s):
#         if i.isupper():
#             r = 'True'
#             break
#     expect_result.append(r)

#     expect_result = '\n'.join(expect_result)
#     print(expect_result)

# def print_formatted(number: int):

#     dec_num = []
#     oct_num = []
#     hex_num = []
#     bin_num = []
#     for i in range(1, number + 1):
#         dec_num.append(str(i))
#         oct_num.append(oct(i)[2:])
#         hex_num.append(hex(i)[2:].upper())
#         bin_num.append(bin(i)[2:])
#     mbin_len = len(bin(number)[2:])
#     for i in range(0, number):
#         len_dec = mbin_len - (len(dec_num[i])-1)
#         len_oct = mbin_len - (len(oct_num[i])-1)
#         len_hex = mbin_len - (len(hex_num[i])-1)
#         len_bin = mbin_len - (len(bin_num[i])-1)
#         num_index = f'{" " * (len_dec-1)}{dec_num[i]}{" " * len_oct}{oct_num[i]}{" " * len_hex}{hex_num[i]}{" " * len_bin}{bin_num[i]}'
#         print(num_index)


# if __name__ == '__main__':
#     # n = int(input())
#     print_formatted(99)


# def print_formatted(number):
#     # your code goes here
#     for i in range(1, number+1):
#         l=len('{0:b}'.format(number))
#         l=int(l)
#         print('{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(i,width=l))

# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)

# if __name__ == '__main__':
#     n = int(input())
#     list_n = []
#     while n > 0:
#         i = n - 1
#         list_n.append(i)
#         n = i
#     list_n = list_n[::-1]
#     for i in list_n:
#         print(f"{i*i}")


# def swap_case(s):
#     list_s = list(s)
#     list_exp = []
#     for i in list_s:
#         if i.isupper():
#             list_exp.append(i.lower())
#         else:
#             list_exp.append(i.upper())
#     text = ''.join(list_exp)
#     return text

# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)


# if __name__ == '__main__':
#     n = int(input())
#     for i in range(n):
#         try:
#             x, y = input().split()
#             x = int(x)
#             y = int(y)
#             print(x // y)
#         except ZeroDivisionError as e:
#             print(f"Error Code: {e}")
#         except ValueError as e:
#             print(f"Error Code: {e}")


# def print_formatted(number: int):
#     # Tạo danh sách cho các hệ thống số
#     dec_num = []
#     oct_num = []
#     hex_num = []
#     bin_num = []
    
#     # Điền dữ liệu vào các danh sách
#     for i in range(1, number + 1):
#         dec_num.append(str(i))
#         oct_num.append(oct(i)[2:])
#         hex_num.append(hex(i)[2:].upper())  # Chuyển đổi chữ cái thành chữ hoa
#         bin_num.append(bin(i)[2:])
    
#     # Tính độ dài của số nhị phân lớn nhất để căn chỉnh
#     mbin_len = len(bin(number)[2:])
    
#     # In các số đã được căn chỉnh
#     for i in range(number):
#         len_dec = len(dec_num[i])
#         len_oct = len(oct_num[i])
#         len_hex = len(hex_num[i])
#         len_bin = len(bin_num[i])

#         # Căn chỉnh và in từng số
#         num_index = f'{" " * (mbin_len - len_dec)}{dec_num[i]}'
#         num_index += f'{" " * (mbin_len - len_oct)}{oct_num[i]}'
#         num_index += f'{" " * (mbin_len - len_hex)}{hex_num[i]}'
#         num_index += f'{" " * (mbin_len - len_bin)}{bin_num[i]}'
#         print(num_index)

# # Test the function
# print_formatted(5)

# Complete the solve function below.
# def solve(s):
#     """
#     """
#     conv_list = list(s)
#     for i in range(len(conv_list)):
#         if conv_list[i] == ' ':
#             conv_list[i+1] = conv_list[i+1].upper()
#     for i in range(len(conv_list)):
#         if conv_list[i].isalpha():
#             conv_list[i] = conv_list[i].upper()
#             break
#     exp_str = ''.join(conv_list)
#     return exp_str


# if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()

    # result = solve(s)

    # fptr.write(result + '\n')

    # fptr.close()

# def average(array):
#     # your code goes here
#     arr = set(array)
#     exp_result = float(sum(arr))/len(arr)
#     return exp_result
# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = average(arr)
#     print(result)


# from itertools import permutations
# if __name__ == '__main__':
#     s = input()
#     n = int(input())
#     exp_result = ''
#     for i in permutations(sorted(s), n):
#         exp_result += ''.join(i) + '\n'
#     print(exp_result)


# n = int(input())
# s = set(map(int, input().split()))

# for i in range(int(input())):
#     command = input().split()
#     if command[0] == 'pop':
#         s.pop()
#     elif command[0] == 'remove':
#         s.remove(int(command[1]))
#     elif command[0] == 'discard':
#         s.discard(int(command[1]))

# print(sum(s))


# n1 = int(input())
# n2 = int(input())
# a = n1//n2
# b = n1%n2
# print(f"({a}, {b})")


# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
# a = pow(n1, n2)
# b = pow(n1, n2, n3)
# print(a)
# print(b)


# n_list = []
# for i in range(4):
#     n = int(input())
#     n_list.append(n)

# n1 = pow(n_list[0], n_list[1]) + pow(n_list[2], n_list[3])
# print(n1)

# n = int(input())
# s = set(map(int, input().split()))

# for i in range(int(input())):
#     command = input().split()
#     u = set(map(int, input().split()))
#     if command[0] == 'intersection_update':
#         s.intersection_update(u)
#     elif command[0] == 'update':
#         s.update(u)
#     elif command[0] == 'symmetric_difference_update':
#         s.symmetric_difference_update(u)
#     elif command[0] == 'difference_update':
#         s.difference_update(u)
# print(sum(s))

# for i in range(int(input())):
#     n1 = int(input())
#     u1 = set(map(int, input().split()))
#     n2 = int(input())
#     u2 = set(map(int, input().split()))
#     if u1.issubset(u2):
#         print(True)
#     else:
#         print(False)


# num_index = input().split()
# total_list = []
# for i in range(int(num_index[1])):
#     num_list = list(map(float, input().split()))
#     total_list.append(num_list)
# zip_tup = list(zip(*total_list))
# for i in range(int(num_index[0])):
#     print(sum(zip_tup[i])/int(num_index[1]))


# x, k = list(map(int,input().split()))
# p = eval(input())
# if p == k:
#     print(True)
# else:
#     print(False)


# e_num = int(input())
# e_stu = set(map(int, input().split()))
# f_num = int(input())
# f_stu = set(map(int, input().split()))

# print(len(e_stu.difference(f_stu)))


# if __name__ == '__main__':
#     nm = input().split()
#     n = int(nm[0])
#     m = int(nm[1])
#     arr = []
#     for _ in range(n):
#         arr.append(list(map(int, input().rstrip().split())))
#     k = int(input())

#     for i in range(n - 1):
#         for j in range(n - i - 1):
#             if arr[j][k] > arr[j + 1][k]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     exp_arr = ''
#     for i in arr:
#         exp_arr += ' '.join(map(str, i)) + "\n"
#     print(exp_arr)

# def check_palindromic(p):
#     p_list = []
#     for i in p:
#         if str(i) == str(i)[::-1]:
#             p_list.append(True)
#         elif i < 0:
#             return False
#         else:
#             p_list.append(False)
#     if True in p_list:
#         return True
#     else:
#         return False

# if __name__ == '__main__':
#     n = int(input())
#     p = list(map(int, input().split()))
#     exp_result = check_palindromic(p)
#     print(exp_result)

# if __name__ == '__main__':
#     m = int(input())
#     for i in range(m):
#         n = input()
#         try:
#             if '.' in n:
#                 n = float(n)
#                 print(True)
#             else:
#                 print(False)
#         except ValueError:
#             print(False)

# def bubble_sort(arr):
#     for i in range(len(arr) - 1):
#         for j in range(len(arr) - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr

# if __name__ == '__main__':
#     n = input()
#     n_len = len(n)
#     s_list = list(n)
#     num_list = []
#     text_list = []
#     for i in range(n_len):
#         if s_list[i].isdigit():
#             num_list.append(s_list[i])
#         else:
#             text_list.append(s_list[i])
#     upper_text = []
#     lower_text = []
#     odd_num = []
#     even_num = []
#     for i in range(len(text_list)):
#         if text_list[i].isupper():
#             upper_text.append(text_list[i])
#         else:
#             lower_text.append(text_list[i])

#     for i in range(len(num_list)):
#         if int(num_list[i])%2 == 0:
#             even_num.append(int(num_list[i]))
#         else:
#             odd_num.append(int(num_list[i]))
#     lower_text = bubble_sort(lower_text)
#     upper_text = bubble_sort(upper_text)
#     odd_num = bubble_sort(odd_num)
#     even_num = bubble_sort(even_num)
#     sorted_num = list(map(str, odd_num)) + list(map(str, even_num))
#     exp_list = lower_text + upper_text + sorted_num
#     exp_str = ''.join(exp_list)
#     print(exp_str)

# regex_pattern = r"\D"   # Do not delete 'r'.

# import re
# print("\n".join(re.split(regex_pattern, input())))


# if __name__ == '__main__':
#     thickness = int(input()) #This must be an odd number
#     c = 'H'

#     #Top Cone
#     for i in range(thickness):
#         print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#     #Top Pillars
#     for i in range(thickness+1):
#         print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#     #Middle Belt
#     for i in range((thickness+1)//2):
#         print((c*thickness*5).center(thickness*6))

#     #Bottom Pillars
#     for i in range(thickness+1):
#         print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#     #Bottom Cone
#     for i in range(thickness):
#         print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# if __name__ == '__main__':
#     nm = input().split()
#     n = int(nm[0])
#     m = int(nm[1])
#     a = []
#     b = []
#     for i in range(n):
#         text = input()
#         a.append(text)
#     for i in range(m):
#         text = input()
#         b.append(text)
#     exp_results = []
#     for i in range(m):
#         for j in range(n):
#             if b[i] == a[j]:
#                 exp_results.append(f"{j+1}")
#             elif b[i] not in a:
#                 exp_results.append("-1")
#                 break
#         print(" ".join(exp_results))
#         exp_results.clear()

# import calendar
# l_in = list(map(int,input().split()))
# a = calendar.weekday(l_in[2], l_in[0], l_in[1])
# days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
# print(days[a])


# from collections import deque

# n = int(input())
# a = deque([])
# for i in range(n):
#     cmd_in = input().split()
#     c = str(cmd_in[0])
#     if len(cmd_in) == 2:
#         n = int(cmd_in[1])
#     if 'appendleft' == c:
#         a.appendleft(n)
#     elif 'append' == c:
#         a.append(n)
#     elif 'pop' == c:
#         a.pop()
#     elif 'popleft' == c:
#         a.popleft()

# print(' '.join(map(str, a)))

# if __name__ == '__main__':
#     e = int(input())
#     stu_e = list(map(int, input().split()))
#     f = int(input())
#     stu_f = list(map(int, input().split()))
#     exp_results = []
#     for i in stu_e:
#         if i in stu_f and i not in exp_results:
#             exp_results.append(i)
#     print(len(exp_results))


# if __name__ == '__main__':
#     n = input()
#     set_n = set(map(int, input().split()))
#     m = input()
#     set_m = set(map(int, input().split()))
#     diff_n = set_n.difference(set_m)
#     diff_m = set_m.difference(set_n)
#     diff_n.update(diff_m)
#     diff_n = list(diff_n)
#     for i in range(len(diff_n) - 1):
#         for j in range(len(diff_n) - i -1):
#             if diff_n[j] > diff_n[j+1]:
#                 diff_n[j], diff_n[j + 1] = diff_n[j + 1] , diff_n[j]
#     for i in diff_n:
#         print(i)


# from itertools import combinations

# if __name__ == '__main__':
#     text_in = input().split()
#     t = str(text_in[0])
#     n = int(text_in[1])
#     a = reversed(list(range(n)))
#     for i in a:
#         combi = sorted((list(combinations(t, n - i))))
#         for j in combi:
#             print(''.join(j))
