import math

english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet_text = ''


def encode(text_to_encode: str, encode_key_a: list, encode_key_b: list) -> str:
    """encode text_to_encode and return encryption_text"""
    encryption_text = ''
    for i in range(0, len(text_to_encode)):
        if i > 1:
            encode_key_a.append((encode_key_a[i - 1] * encode_key_a[i - 2]) % len(alphabet_text))
            encode_key_b.append((encode_key_b[i - 1] + encode_key_b[i - 2]) % len(alphabet_text))

        if alphabet_text.find(text_to_encode[i]) != -1:
            encryption_text += alphabet_text[((encode_key_a[i] * alphabet_text.find(text_to_encode[i])
                                               + encode_key_b[i]) % len(alphabet_text))]
        else:
            encryption_text += '?'

    return encryption_text


def decode(text_to_decode: str, decode_key_a: list, decode_key_b: list) -> str:
    """decode text_to_decode and return decryption_text"""
    decryption_text = ''
    for i in range(0, len(text_to_decode)):
        if i > 1:
            decode_key_a.append((decode_key_a[i - 1] * decode_key_a[i - 2]) % len(alphabet_text))
            decode_key_b.append((decode_key_b[i - 1] + decode_key_b[i - 2]) % len(alphabet_text))
        else:
            decode_key_a[i] = euclid_alg(decode_key_a[i], len(alphabet_text))

        if alphabet_text.find(text_to_decode[i]) != -1:
            decryption_text += alphabet_text[((alphabet_text.find(text_to_decode[i]) - decode_key_b[i])
                                          * decode_key_a[i]) % len(alphabet_text)]
        else:
            decryption_text += '?'

    return decryption_text


def euclid_alg(a: int, p: int) -> int:
    """return modular inverse of A mod P"""
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

    first_key = input(f'\nВведите сначала первую пару ключей через пробел, затем вторую'
                      f'\nчисловые значения ключа должны быть '
                      f'взаимнопросты с числом {len(alphabet_text)}\n').split()
    key = [(int(item) % len(alphabet_text)) for item in first_key]

    if (len(key) != 4 or math.gcd(key[0], len(alphabet_text)) != 1) or \
            ((key[1] != 0) and (math.gcd(key[1], len(alphabet_text)) != 1)) or \
            (math.gcd(key[2], len(alphabet_text)) != 1) or \
            ((key[3] != 0) and (math.gcd(key[3], len(alphabet_text)) != 1)):
        print("\nОшибка, неверные ключи")
        exit()

    if operation == 1:
        plain_text = input(f'\nВведите открытый текст, состоящий из символов "{alphabet_text}": \n')
        print(f'полученный шифр текст:\n{encode(plain_text, key[::2], key[1::2])}')
    else:
        plain_text = input(f'\nВведите шифр текст, состоящий из символов "{alphabet_text}":\n')
        print(f'полученный открытый текст:\n{decode(plain_text, key[::2], key[1::2])}')