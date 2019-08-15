from alphabet import alphabet

def ceasar_cipher(key, message):
    if type(key) is list:
        return ceasar_cipher_with_list(key, message)
    else:
        return simple_ceasar_cipher(key, message)

def ceasar_cipher_with_list(key, message):
    return 'Not implemented yet'

def result(letter, key, uppercase=False):
    letter_result = _alphabet[ord(_alphabet[0]) - ord(letter.lower())]

    if uppercase:
        letter_result.upper()

    return chr(ord(letter_result) + key)

def simple_ceasar_cipher(key, message):
    final_message = ''

    for letter in message:
        if letter is not ' ':
            letter = result(letter, key, letter.isupper())

        final_message += letter

    return final_message

if __name__ == '__main__':
    key = int(input())
    message = input()
    _alphabet = alphabet(key//26 + 2)

    print(ceasar_cipher(key, message))
