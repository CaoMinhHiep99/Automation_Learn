def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Phần tử hiện tại cần chèn
        j = i - 1
        # Di chuyển các phần tử của arr[0..i-1] lớn hơn key lên một vị trí phía trước
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # Chèn phần tử key vào vị trí phù hợp
        arr[j + 1] = key
    return arr


if __name__ == '__main__':
    array = [12, 11, 13, 5, 6]
    arr = insertion_sort(array)
    print(f'Array after selection sort: {arr}')
