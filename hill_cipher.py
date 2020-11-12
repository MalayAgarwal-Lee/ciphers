def pad_text(text, key):
    original_len = len(text)
    remainder = original_len % len(key)
    if remainder != 0:
        text += "Z" * remainder
    return text, original_len


def multiply_matrices(x, y):
    result = []
    y_len = len(y)
    for row in x:
        result.append(sum(row[i] * y[i] for i in range(y_len)))
    return [value % 26 for value in result]


def encrypt(text, key):
    result = ''
    key_len, text_len = len(key), len(text)
    start, end = 0, key_len
    while start < text_len:
        offsets = [ord(char) - 65 for char in text[start:end]]
        encrypted_text = multiply_matrices(key, offsets)
        result += ''.join(chr(char + 65) for char in encrypted_text)
        start, end = start + key_len, end + key_len
    return result


def main():
    text = input("Enter the text (without space): ").upper()
    key = [[9, 4], [5, 7]]
    text, original_len = pad_text(text, key)
    result = encrypt(text, key)
    print(result[:original_len])


if __name__ == "__main__":
    main()
