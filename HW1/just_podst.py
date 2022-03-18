
english_alphabet = 'abcdefghijklmnopqrstufvxyz'
russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet_text = ''


def encode(text_to_encode, encode_key):
    """encode text_to_encode and return encryption_text"""
    encryption_text = ''
    for i in range(0, len(text_to_encode)):
        encryption_text += encode_key[alphabet_text.find(text_to_encode[i % len(alphabet_text)])]
    return encryption_text


def decode(text_to_decode, decode_key):
    """decode text_to_decode and return decryption_text"""
    decryption_text = ''
    for i in range(0, len(text_to_decode)):
        decryption_text += alphabet_text[decode_key.find(text_to_decode[i % len(alphabet_text)])]
    return decryption_text


if __name__ == '__main__':
    language = input('\n[1] Русский алфавит или [2] Английский алфавит \nВведите цифру нужного алфавита: ')
    if language == '1':
        alphabet_text = russian_alphabet
    elif language == '2':
        alphabet_text = english_alphabet
    else:
        print("\nОшибка, неизвестный алфавит")
        exit()

    operation = input('\n[1] Зашифрование или [2] Расшифрование\nВведите цифру нужной операции: ')
    if operation == '1':
        plain_text = input('\nВведите открытый текст: \n')
        key = input(f'\nВведите ключ:\n{alphabet_text}\n')
        print(f'\nполученный шифр текст:\n{encode(plain_text, key)}')
    elif operation == '2':
        plain_text = input('\nВведите шифр текст: \n')
        key = input(f'\nВведите ключ:\n{alphabet_text}\n')
        print(f'\nполученный открытый текст:\n{decode(plain_text, key)}')
    else:
        print("\nОшибка, неизвестная операция")
