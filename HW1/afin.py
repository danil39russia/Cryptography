import math

english_alphabet = 'abcdefghijklmnopqrstufvxyz'
russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet_text = ''


def encode(text_to_encode: str, encode_key: list) -> str:
    """encode text_to_encode and return encryption_text"""
    encryption_text = ''
    for i in range(0, len(text_to_encode)):
        encryption_text += alphabet_text[((encode_key[0] * alphabet_text.find(text_to_encode[i]) + encode_key[1])
                                          % len(alphabet_text))]
    return encryption_text


def decode(text_to_decode: str, decode_key: list) -> str:
    """decode text_to_decode and return decryption_text"""
    decryption_text = ''
    for i in range(0, len(text_to_decode)):
        decryption_text += alphabet_text[((alphabet_text.find(text_to_decode[i]) - decode_key[1])
                                          * euclid_alg(decode_key[0], len(alphabet_text)))
                                         % len(alphabet_text)]
    return decryption_text


def euclid_alg(a: int, p: int) -> str:
    y2 = 0
    y1 = 1
    if a > p:
        c = a
        a = p
        p = c
    r = None
    while r != 0:
        q = p // a
        r = p % a
        y = y2 - q * y1
        p = a
        a = r
        y2 = y1
        y1 = y
    return y2


if __name__ == '__main__':
    language = int(input('\n[1] Русский алфавит или [2] Английский алфавит \nВведите цифру нужного алфавита: '))
    if language == 1:
        alphabet_text = russian_alphabet
    elif language == 2:
        alphabet_text = english_alphabet
    else:
        print("\nОшибка, неизвестный алфавит")
        exit()

    operation = int(input('\n[1] Зашифрование или [2] Расшифрование\nВведите цифру нужной операции: '))
    if operation != 1 and operation != 2:
        print("\nОшибка, неизвестная операция")
        exit()

    first_key = input(f'\nВведите ключ состоящий из двух цифр через пробел,\nчисловые значения '
                      f'ключа должны быть взаимнопросты с {len(alphabet_text)}\n').split()
    key = [(int(item) % len(alphabet_text)) for item in first_key]

    if (math.gcd(key[0], len(alphabet_text)) != 1) or \
            ((key[1] != 0) and (math.gcd(key[1], len(alphabet_text)) != 1)) \
            or len(key) != 2:
        print("\nОшибка, неверные ключи")
        exit()

    if operation == 1:
        plain_text = input(f'\nВведите открытый текст, состоящий из символов "{alphabet_text}": \n')
        print(f'\nПолученный шифр текст:\n{encode(plain_text, key)}')
    else:
        plain_text = input(f'\nВведите шифр текст, состоящий из символов "{alphabet_text}": \n')
        print(f'\nПолученный открытый текст:\n{decode(plain_text, key)}')