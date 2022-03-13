
english_alphabet = 'abcdefghijklmnopqrstufvxyz'
russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

while __name__ == '__main__':

    language = input('\n[1] Русский алфавит или [2] Английский алфавит \nВведите цифру нужного алфавита:\n')

    if language == '1':
        alphabet_text = russian_alphabet
    elif language == '2':
        alphabet_text = english_alphabet
    else:
        print("\nОшибка, неизвестный алфавит")
        __name__ = '__main__'
        continue

    entered_list = input('Введите символы через пробел: \n').split()

    for i in entered_list:
        if i.isalpha():
            if (alphabet_text.find(i) != -1):
                print(alphabet_text.find(i), end=' ')
            else:
                print('?', end=' ')
        elif i.isnumeric():
            print(alphabet_text[int(i)%len(alphabet_text)], end=' ')
        else: print('?', end=' ')

    print("\n\nКонец работы")