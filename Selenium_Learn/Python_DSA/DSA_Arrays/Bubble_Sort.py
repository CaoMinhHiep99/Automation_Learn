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

def print_formatted(number: int):

    dec_num = []
    oct_num = []
    hex_num = []
    bin_num = []
    for i in range(1, number + 1):
        dec_num.append(str(i))
        oct_num.append(oct(i)[2:])
        hex_num.append(hex(i)[2:].upper())
        bin_num.append(bin(i)[2:])
    mbin_len = len(bin(number)[2:])
    for i in range(0, number):
        len_dec = mbin_len - (len(dec_num[i])-1)
        len_oct = mbin_len - (len(oct_num[i])-1)
        len_hex = mbin_len - (len(hex_num[i])-1)
        len_bin = mbin_len - (len(bin_num[i])-1)
        num_index = f'{" " * (len_dec-1)}{dec_num[i]}{" " * len_oct}{oct_num[i]}{" " * len_hex}{hex_num[i]}{" " * len_bin}{bin_num[i]}'
        print(num_index)


if __name__ == '__main__':
    # n = int(input())
    print_formatted(99)


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
