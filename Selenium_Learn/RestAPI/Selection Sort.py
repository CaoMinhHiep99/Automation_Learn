def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Giả sử phần tử đầu tiên của vùng chưa sắp xếp là phần tử nhỏ nhất
        min_index = i
        # Tìm phần tử nhỏ nhất trong vùng chưa sắp xếp
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Hoán đổi phần tử nhỏ nhất với phần tử đầu của vùng chưa sắp xếp
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


if __name__ == '__main__':
    array = [64, 25, 12, 22, 11]
    arr = selection_sort(array)
    print(f'Array after selection sort: {arr}')