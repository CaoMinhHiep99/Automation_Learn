def binary_search(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2
        # Kiểm tra nếu phần tử giữa là giá trị cần tìm
        if arr[mid] == target:
            return mid
        # Nếu giá trị cần tìm nhỏ hơn phần tử giữa, tìm trong nửa bên trái
        elif arr[mid] > target:
            return binary_search(arr, target, low, mid - 1)
        # Nếu giá trị cần tìm lớn hơn phần tử giữa, tìm trong nửa bên phải
        else:
            return binary_search(arr, target, mid + 1, high)
    else:
        return -1  # Trả về -1 nếu không tìm thấy

def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        # Kiểm tra nếu phần tử giữa là giá trị cần tìm
        if arr[mid] == target:
            return mid
        # Nếu giá trị cần tìm nhỏ hơn phần tử giữa, tìm trong nửa bên trái
        elif arr[mid] > target:
            high = mid - 1
        # Nếu giá trị cần tìm lớn hơn phần tử giữa, tìm trong nửa bên phải
        else:
            low = mid + 1
    return -1  # Trả về -1 nếu không tìm thấy


array = [1, 3, 5, 7, 9, 11, 13]
target = 7

# Sử dụng phiên bản đệ quy
result_recursive = binary_search(array, target, 0, len(array) - 1)
if result_recursive != -1:
    print(f"Giá trị {target} được tìm thấy tại chỉ số {result_recursive} (đệ quy).")
else:
    print(f"Giá trị {target} không có trong mảng (đệ quy).")

# Sử dụng phiên bản vòng lặp
result_iterative = binary_search_iterative(array, target)
if result_iterative != -1:
    print(f"Giá trị {target} được tìm thấy tại chỉ số {result_iterative} (vòng lặp).")
else:
    print(f"Giá trị {target} không có trong mảng (vòng lặp).")
