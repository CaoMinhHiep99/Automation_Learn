def counting_sort(arr):
    # Tìm giá trị lớn nhất trong mảng
    max_val = max(arr)
    # Tạo mảng đếm (count) với các phần tử ban đầu là 0
    count = [0] * (max_val + 1)
    # Đếm số lần xuất hiện của mỗi phần tử
    for num in arr:
        count[num] += 1
    # Tính vị trí của từng phần tử dựa trên mảng count
    index = 0
    for i in range(len(count)):
        while count[i] > 0:
            arr[index] = i
            index += 1
            count[i] -= 1
    return arr


if __name__ == '__main__':
    array = [4, 2, 2, 8, 3, 3, 1, 1, 8, 8, 8, 2, 2, 10, 10, 9, 9]
    arr = counting_sort(array)
    print(f'Array after selection sort: {arr}')