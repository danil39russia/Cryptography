english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet_text = ''


def text_to_num(text: str):
    num_text = []
    for i in text:
        if alphabet_text.find(i) != -1:
            num_text.append(alphabet_text.find(i))
        else:
            num_text.append("?")
    return num_text


def num_to_text(num) -> str:
    text = ''
    for i in num:
        if type(i) == int or i.isnumeric():
            text += alphabet_text[int(i) % len(alphabet_text)]
        else:
            text += '?'
    return text


def encode(text_to_encode: str) -> str:
    """encode text_to_encode and return encryption_text"""
    encryption_text = []
    num_text_to_encode = text_to_num(text_to_encode)
    for i in range(0, len(text_to_encode)):
        encryption_text.append(num_text_to_encode[i] + key[i])
    return num_to_text(encryption_text)


def decode(text_to_decode: str) -> str:
    """decode text_to_decode and return decryption_text"""
    decryption_text = []
    num_text_to_encode = text_to_num(text_to_decode)
    for i in range(0, len(text_to_decode)):
        decryption_text.append(num_text_to_encode[i] - key[i])
    return num_to_text(decryption_text)


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

    key1 = input(f'\nВведите ключ:\n')
    key = key1

    if operation == 1:
        plain_text = input(f'\nВведите открытый текст, состоящий из символов "{alphabet_text}": \n')
        while len(plain_text) - len(key) > 0:
            key += key1
        key = text_to_num(key)
        print(key)
        print(f'\nПолученный шифр текст:\n{encode(plain_text)}')
    else:
        plain_text = input(f'\nВведите шифр текст, состоящий из символов "{alphabet_text}":\n')
        while len(plain_text) - len(key) > 0:
            key += key1
        key = text_to_num(key)
        print(key)
        print(f'\nПолученный открытый текст:\n{decode(plain_text)}')
