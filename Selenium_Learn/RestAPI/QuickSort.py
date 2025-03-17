def quicksort(arr):
    if len(arr) <= 1:  # Nếu mảng có 1 hoặc 0 phần tử, xem như đã sắp xếp
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Chọn pivot là phần tử giữa mảng
        left = [x for x in arr if x < pivot]  # Mảng các phần tử nhỏ hơn pivot
        middle = [x for x in arr if x == pivot]  # Mảng các phần tử bằng pivot
        right = [x for x in arr if x > pivot]  # Mảng các phần tử lớn hơn pivot
        # Đệ quy sắp xếp các phần tử trong left và right, rồi ghép lại
        return quicksort(left) + middle + quicksort(right)


if __name__ == '__main__':
    array = [3, 6, 8, 10, 1, 2, 1]
    arr = quicksort(array)
    print(f'Array after selection sort: {arr}')



def median_of_three(arr, low, high):
    mid = (low + high) // 2
    a, b, c = arr[low], arr[mid], arr[high]
    if a > b:
        a, b = b, a
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    return b



def quicksort_median_of_three(arr):
    if len(arr) <= 1:
        return arr
    pivot = median_of_three(arr, 0, len(arr) - 1)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print(".........")
    print(f'Left: {left}')
    print(f'Middle: {middle}')
    print(f'Right: {right}')
    return quicksort_median_of_three(left) + middle + quicksort_median_of_three(right)


if __name__ == '__main__':
    array = [3, 6, 8, 10, 1, 2, 1, 11, 23, 31, 41, 12, 67, 34, 14]
    arr = quicksort_median_of_three(array)
    print(f'Array after selection sort: {arr}')