
english_alphabet = 'abcdefghijklmnopqrstufvxyz'
russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def encode(plain_text, key):
    encryption_text = ''
    for i in range (0, len(plain_text)):
        encryption_text += key[alphabet_text.find(plain_text[i])]
    return encryption_text

def decode(plain_text, key):
    decryption_text = ''
    for i in range (0, len(plain_text)):
        decryption_text += alphabet_text[key.find(plain_text[i])]
    return decryption_text

if __name__ == '__main__':
    language = input('[1] Русский алфавит или [2] Английский алфавит \nВведите цифру нужного алфавита: ')
    if language == '1':
        alphabet_text = russian_alphabet
    elif language == '2':
        alphabet_text = english_alphabet
    else:
        print("Ошибка, неизвестный алфавит")
        exit()
    operation = input('[1] Зашифрование или [2] Расшифрование\nВведите цифру нужной операции: ')
    if operation == '1':
        plain_text = input('Введите открытый текст: \n')
        key = input(f'Введите ключ:\n{alphabet_text}\n')
        print(f'полученный шифр текст:\n{encode(plain_text, key)}')
    elif operation == '2':
        plain_text = input('Введите шифр текст: \n')
        key = input(f'Введите ключ:\n{alphabet_text}\n')
        print(f'полученный открытый текст:\n{decode(plain_text, key)}')
    else: print("Ошибка, неизвестная операция")