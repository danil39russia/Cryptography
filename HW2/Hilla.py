import math
import numpy as np

english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet_text = ''


def text_to_num(text):
    num_text = []
    for i in text:
        if alphabet_text.find(i) != -1:
            num_text.append(alphabet_text.find(i))
        else:
            num_text.append("x")
    return num_text


def num_to_text(num):
    text = ''
    for i in range(0, len(num)):
        ch = (num[i] % len(alphabet_text))
        x = ch[0] % 1
        if x > 0.5:
            x = int(ch[0])+1
        else:
            x = int(ch[0])
        text += alphabet_text[x % len(alphabet_text)]
    return text


def encode(text_to_encode: str) -> str:
    """encode text_to_encode and return encryption_text"""
    encryption_text = ''
    i = 0
    while (block_len*i) + block_len <= len(text_to_encode):
        text_block = text_to_num(text_to_encode[(block_len*i):(block_len*i) + block_len])
        matrix_text = np.matrix(text_block).T
        num = key.dot(matrix_text.astype(int))
        encryption_text += num_to_text(num)
        i += 1
    return encryption_text


def decode(text_to_decode: str) -> str:
    """decode text_to_decode and return decryption_text"""
    decryption_text = ''
    i = 0
    while (block_len*i) + block_len <= len(text_to_decode):
        text_block = text_to_num(text_to_decode[(block_len*i):(block_len*i) + block_len])
        matrix_text = np.matrix(text_block).T
        obr = np.linalg.inv(key)
        num = obr.dot(matrix_text.astype(float))
        decryption_text += num_to_text(num)
        i += 1
    return decryption_text


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

    first_key = input(f'\nВведите невырожденную квадратную матрицу-ключ:\n')
    key = np.matrix(first_key)
    print(f'Обратная матрица:\n{np.linalg.inv(key)}')

    if round(np.linalg.det(key), 3) == 0 or key.shape[0] != key.shape[1] or \
            (round(np.linalg.det(key), 3) != 1 and math.gcd(int(np.linalg.det(key))%len(alphabet_text),
                                                             len(alphabet_text)) != 1):
        print("\nОшибка, неверный ключ")
        exit()

    block_len = key.shape[0]

    if operation == 1:
        plain_text = input(f'\nВведите открытый текст, состоящий из символов "{alphabet_text}": \n')
        while len(plain_text) % block_len != 0:
            plain_text += alphabet_text[0]
        print(f'\nПолученный шифр текст:\n{encode(plain_text)}')
    else:
        plain_text = input(f'\nВведите шифр текст, состоящий из символов "{alphabet_text}":\n')
        while len(plain_text) % block_len != 0:
            plain_text += alphabet_text[0]
        print(f'\nПолученный открытый текст:\n{decode(plain_text)}')
