alphabet_text = 'abcdefghijklmnopqrstuvwxyz'

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
        print(f'i{i}')
        print(f'num_text_to_encode[i]{num_text_to_encode[i]}')
        print(f'key[i]{key[i]}')
        if len(key) < len(text_to_encode):
            key.append((num_text_to_encode[i] + key[i])%len(alphabet_text))
        print(key)
    return num_to_text(encryption_text)


key = 'password'

key = text_to_num(key)

encrypt_text = 'xczwyykkfubkbclohuvcfkhcun'
decrypt_text = 'icheckthiscodebecauseiwont'

if 1:
    encrypt_text = encode(encrypt_text)
    print(encrypt_text)