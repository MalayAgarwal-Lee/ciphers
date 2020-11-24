def pad_text(text, key):
    '''
    Function which pads the plaintext when the text is indivisible by key

    Arguments:
        text: str, the text to be padded
        key: list, the key being used

    Returns:
        The padded text and its length before padding
    '''
    original_len = len(text)
    remainder = original_len % len(key)
    if remainder != 0:
        text += "Z" * (len(key) - remainder)
    return text, original_len


def multiply_matrices(x, y):
    '''
    Function which multiplies a matrix, x with a column matrix, y (mod 26)

    Arguments:
        x: list, a square matrix
        y: list, a column matrix

    Returns:
        The resultant column matrix
    '''
    result = []
    y_len = len(y)
    for row in x:
        result.append(sum(row[i] * y[i] for i in range(y_len)))
    return [value % 26 for value in result]


def encrypt(text, key):
    '''
    Function which encrypts a plaintext according to a key

    Arguments:
        text: str, the plaintext
        key: list, the key to be used

    Returns:
        The encrypted text
    '''
    result = ''
    key_len, text_len = len(key), len(text)
    for start in range(0, text_len, key_len):
        offsets = [ord(char) - 65 for char in text[start:start + key_len]]
        encrypted_text = multiply_matrices(key, offsets)
        result += ''.join(chr(char + 65) for char in encrypted_text)
    return result


def main():
    text = input("Enter the text (without space): ").upper()
    key = [[9, 4], [5, 7]]
    text, original_len = pad_text(text, key)
    result = encrypt(text, key)
    print(result[:original_len])


if __name__ == "__main__":
    main()
