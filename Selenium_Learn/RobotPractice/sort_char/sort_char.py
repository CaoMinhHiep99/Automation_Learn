def sort_char(chars):
    str = []
    num = []

    for char in chars:
        if char.isalpha():
            str.append(char)
        else:
            num.append(char)

    print(f'str: {str}, num:{num}')

    str = ''.join(str)
    num = ''.join(num)

    output = f'{str}{num}'
    print(f'output:{output}')
    return output

if __name__ == "__main__":
    str = "A1B2C3"
    print(sort_char(str))