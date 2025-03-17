def split_string(chars):
    output = chars.split()[-1]
    print(output)

if __name__ == "__main__":
    str = "I'm from USA"
    print(split_string(str))