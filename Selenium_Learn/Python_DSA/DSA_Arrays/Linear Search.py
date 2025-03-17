def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i  # Trả về vị trí của phần tử tìm thấy
    return -1  # Trả về -1 nếu không tìm thấy phần tử

# Sử dụng hàm:
arr = [3, 5, 2, 4, 9]
x = 4
result = linear_search(arr, x)
print("Phần tử cần tìm có tại vị trí:", result) if result != -1 else print("Không tìm thấy phần tử")
