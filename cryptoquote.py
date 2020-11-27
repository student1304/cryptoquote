import random
import sys


def encrypt(quote):
    quote = quote.replace(',', '').replace('.', '').replace("'", '').upper()
    words = quote.split()

    letters = list()
    for letter in quote.replace(' ', ''):
        letters.append(letter)
    letters = set(letters)
    letters = list(letters)

    enc_letters = list(letters)
    random.shuffle(enc_letters)
    enc_quote = list()

    for word in words:
        #print(word)
        new_word = str()
        for l in word:
            #print(l, ':', enc_letters.index(l), '->', letters[enc_letters.index(l)], end=' --- ')
            new_word += letters[enc_letters.index(l)]
            #print(word, '->', new_word, end='---\n')
    
        enc_quote.append(new_word)
    enc_quote_ = ' '.join(word for word in enc_quote)

    #print('Encrypted Quote:', str(enc_quote_))

    return enc_quote_

if __name__ == '__main__':
    """
    Enter a quote in "" to get back an encrypted quote:
    Example:
    python cryptoquote.py "It's a rainy day"
    """
       
    if len(sys.argv) == 1:
        quote = input('Give me a quote to encrypt: ')
    else: 
        quote = sys.argv[1]
    print('Encrypting quote:', quote)
    print('Encrypted quote:', encrypt(quote))