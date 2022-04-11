import math

import numpy as np

english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

true_text = 'хочусамолета'
# отуюсгвншейэ

alphabet_text = ''
key = []
obr = []

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
        if i > 1:
            key.append(key[i-2].dot(key[i-1]))
        num = (key[i].dot(matrix_text.astype(int))) % len(alphabet_text)
        encryption_text += num_to_text(num)
        i += 1
    return encryption_text


if __name__ == '__main__':
    language = int(input('\n[1] Русский алфавит или [2] Английский алфавит \nВведите цифру нужного алфавита: '))
    if language == 1:
        alphabet_text = russian_alphabet
    elif language == 2:
        alphabet_text = english_alphabet
    else:
        print("\nОшибка, неизвестный алфавит")
        exit()

    first_key = '0 1; 1 2'
    key.append(np.matrix(first_key))

    second_key = '0 1; 1 2'
    key.append(np.matrix(first_key))

    block_len = key[0].shape[0]

    if 1:
        plain_text = input(f'\nВведите открытый текст, состоящий из символов "{alphabet_text}": \n')
        while plain_text != true_text:
            print(encode(plain_text))
            plain_text = encode(plain_text)
        print(f'\nПолученный шифр текст:\n{plain_text}')
