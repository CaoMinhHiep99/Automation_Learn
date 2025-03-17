def merge_sort(arr):
    # Nếu mảng chỉ có 1 phần tử hoặc rỗng, xem như đã sắp xếp
    if len(arr) <= 1:
        return arr

    # Chia mảng thành hai nửa
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    print('...........')
    print(f'left_half:{left_half}')
    print(f'right_half:{right_half}')

    # Đệ quy sắp xếp từng nửa
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    print('...........')
    print(f'left_sorted:{left_sorted}')
    print(f'right_sorted:{right_sorted}')

    # Hợp nhất hai nửa đã sắp xếp
    return merge(left_sorted, right_sorted)

def merge(left, right):
    result = []
    i = j = 0

    # So sánh từng phần tử và hợp nhất
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Thêm các phần tử còn lại
    result.extend(left[i:])
    result.extend(right[j:])
    print('...........')
    print(f'result: {result}')

    return result


if __name__ == '__main__':
    array = [38, 43, 27, 3, 9, 82, 10, 12, 22, 33, 65, 31, 11, 25, 42]
    arr = merge_sort(array)
    print(f'Array after selection sort: {arr}')