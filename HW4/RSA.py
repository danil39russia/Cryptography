import random
import time
import math

english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet_text = ''
e, d, n = 17, 1817, 2479

def fast_test_f(it_num: int, exp: int):
    bin_exp = bin(exp - 1)
    for i in range(it_num):
        num = random.randint(2, exp - 1)
        result = num
        for j in range(3, len(bin_exp)):
            result = (result ** 2) % exp
            if int(bin_exp[j]) == 1:
                result = (result * num) % exp
        if result != 1:
            return False
    return True


def fast_exp(num: int, exp: int, mod: int):
    bin_exp = bin(exp)
    result = num
    for j in range(3, len(bin_exp)):
        result = (result ** 2) % mod
        if int(bin_exp[j]) == 1:
            result = (result * num) % mod
    return result


def alg_evclid(a: int, b: int) -> (int, int, int):
    if b > a:
        raise Exception("alg_euclid -> a is lower than b, but must be bigger")
    x2, x1, y2, y1 = 1, 0, 0, 1
    r = None
    while r != 0:
        r = a % b
        q = a // b
        x = x2 - q * x1
        y = y2 - q * y1
        a, b, x2, x1, y2, y1 = b, r, x1, x, y1, y
    d, x, y = a, x2, y2
    return d, x, y


'''
def is_prime(num: int) -> bool:
    divider = 2
    num2 = num ** 0.5
    while divider <= num2 and num % divider != 0:
        divider += 1
    return divider > num2
'''


def generate_keys(length: int) -> (int, int, int):
    length /= 2
    q = random.randint(2 ** (length - 1), 2 ** length)
    p = random.randint(2 ** (length - 1), 2 ** length)
    while not fast_test_f(100, q):
        q = random.randint(2 ** (length - 1), 2 ** length)
    while not fast_test_f(100, p):
        p = random.randint(2 ** (length - 1), 2 ** length)
    n = p * q
    f = (p - 1) * (q - 1)
    e = random.randint(1, f - 1)
    while alg_evclid(f, e)[0] != 1:
        e = random.randint(1, f - 1)
    d = alg_evclid(f, e)[2]
    return e, d, n


def encode(text: str, key_e: int, key_n: int):
    encode_text = ''
    len_enc = int(math.log(key_n, 2))
    while len(text) % len_enc != 0:
        text = '0' + text
    print(text)
    i = 0
    while (i+1)*len_enc <= len(text):
        encode_text += (str(bin(fast_exp(int(text[(i*len_enc):((i+1)*len_enc)], 2), key_e, key_n))[2:]))
        encode_text += ' '
        i += 1
    return encode_text


def decode(text, key_d: int, key_n: int):
    len_enc = int(math.log(key_n, 2))
    decode_text = ''
    for i in text:
        decode_text += str(bin(fast_exp(int(i, 2), key_d, key_n))[2:]).rjust(len_enc, '0')
    print(decode_text[-16*(len(decode_text) // 16)::])
    decode_text = decode_text[-16*(len(decode_text) // 16)::]
    s = ''.join(chr(int(decode_text[i * 16: i * 16+16], 2)) for i in range(len(decode_text) // 16))
    return s

while __name__ == '__main__':
    '''
    language = int(input('\n[1] Русский алфавит или [2] Английский алфавит \nВведите цифру нужного алфавита: '))
    if language == 1:
        alphabet_text = russian_alphabet
    elif language == 2:
        alphabet_text = english_alphabet
    else:
        print("\nОшибка, неизвестный алфавит")
        exit()
    '''

    operation = int(input('\n[1] Зашифрование или [2] Расшифрование\nВведите цифру нужной операции: '))
    if operation != 1 and operation != 2:
        print("\nОшибка, неизвестная операция")
        exit()

    key_operation = int(input('\n[1] Сгенерировать ключ [2] Свой ключ [3] Ничего\nВведите цифру нужной операции: '))
    if key_operation != 1 and key_operation != 2 and key_operation != 3:
        print("\nОшибка, неизвестная операция")
        exit()

    if key_operation == 1:
        key_len = int(input('\nВведите длину ключа цифрами: '))
        start = time.process_time()
        e, d, n = generate_keys(key_len)
        print(time.process_time() - start)
        print(f'\nПара открытый ключ: {e, n}\n'
              f'Пара закрытый ключ: {d, n}')


    if operation == 1:
        if key_operation == 2:
            key = input('\nВведите пару открытого ключа через пробел: ').split()
            e, n = int(key[0]), int(key[1])
        plain_text = input(f'\nВведите открытый текст: \n')
        bits_text = ''.join([bin(ord(c))[2:].rjust(16,'0') for c in plain_text])
        print(bits_text)
        print(f'\nПолученный шифр текст:\n{encode(bits_text, e, n)}')
    else:
        if key_operation == 2:
            key = input('\nВведите пару закрытого ключа через пробел: ').split()
            d, n = int(key[0]), int(key[1])
        plain_text = input(f'\nВведите закрытый текст: \n').split()
        #bits_text = ''.join([bin(ord(c))[2:] for c in plain_text])
        print(f'\nПолученный открытый текст:\n{decode(plain_text, d, n)}')

