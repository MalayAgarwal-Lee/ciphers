from math import ceil

def process_key(text, key):
    key_len, text_len = len(key), len(text)
    if key_len < text_len:
        repeat = ceil(text_len / key_len)
        key = key * repeat
    key = key[:text_len]
    return key


def encrypt(plaintext, key):
    offsets = [
        (ord(pt_char) + ord(key_char)) % 65
        for pt_char, key_char in zip(plaintext, key)
    ]
    offsets = [offset - 26 if offset > 25 else offset for offset in offsets]
    return ''.join(chr(offset + 65) for offset in offsets)


def decrypt(cipher, key):
    offsets = [
        (ord(cp_char) - ord(key_char)) % 26
        for cp_char, key_char in zip(cipher, key)
    ]
    offsets = [offset - 26 if offset > 25 else offset for offset in offsets]
    return ''.join(chr(offset + 65) for offset in offsets)


def make_choice():
    print("1. Encrypt")
    print("2. Decrypt")
    choice = int(input("Enter input: "))
    return bool(choice - 1)


def main():
    choice = make_choice()
    text = input("Enter the text: ").upper()
    key = process_key(text, "LEG")
    result = encrypt(text, key) if not choice else decrypt(text, key)
    print(result)

if __name__ == "__main__":
    main()
