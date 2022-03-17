import math

english_alphabet = 'abcdefghijklmnopqrstufvxyz'
russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def encode(plain_text, keya, keyb):
    """encode plain_text and return encryption_text"""
    encryption_text = ''
    for i in range(0, len(plain_text)):
        encryption_text += alphabet_text[((keya * alphabet_text.find(plain_text[i])
                                           + keyb) % len(alphabet_text))]
    return encryption_text


def decode(plain_text, keya, keyb):
    """decode plain_text and return decryption_text"""
    decryption_text = ''
    for i in range(0, len(plain_text)):
        decryption_text += alphabet_text[((alphabet_text.find(plain_text[i]) -
                                           keyb) * eucl_alg(keya, len(alphabet_text))) % len(alphabet_text)]
    return decryption_text


def eucl_alg(a, p):
    y2 = 0
    y1 = 1
    if a > p:
        c = a
        a = p
        p = c
    r = None
    while r != 0:
        q = p//a
        r = p % a
        y = y2 - q * y1
        p = a
        a = r
        y2 = y1
        y1 = y
    return y2


while __name__ == '__main__':
    language = int(input('\n[1] Русский алфавит или [2] Английский алфавит \nВведите цифру нужного алфавита: '))
    if language == 1:
        alphabet_text = russian_alphabet
    elif language == 2:
        alphabet_text = english_alphabet
    else:
        print("\nОшибка, неизвестный алфавит")
        continue

    operation = int(input('\n[1] Зашифрование или [2] Расшифрование\nВведите цифру нужной операции: '))
    if operation != 1 and operation != 2:
        print("\nОшибка, неизвестная операция")
        continue

    first_key = input(f'\nВведите ключ состоящий из двух цифр через пробел,\nчисловые значения '
                f'ключа должны быть взаимнопросты с {len(alphabet_text)}\n').split()
    key = [(int(item) % len(alphabet_text)) for item in first_key]

    if (math.gcd(key[0], len(alphabet_text)) != 1) or \
            ((key[1] != 0) and (math.gcd(key[1], len(alphabet_text)) != 1))\
            or len(key) != 2:
        print("\nОшибка, неверные ключи")
        continue

    if operation == 1:
        plain_text = input(f'\nВведите открытый текст, состоящий из символов "{alphabet_text}": \n')
        print(f'полученный шифр текст:\n{encode(plain_text, key[0], key[1])}')
    else:
        plain_text = input(f'\nВведите шифр текст, состоящий из символов "{alphabet_text}": \n')
        print(f'полученный открытый текст:\n{decode(plain_text, key[0], key[1])}')