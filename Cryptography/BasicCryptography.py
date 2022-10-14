from random import randrange
def AtbashCryptography(message: str):
    string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join((string[:26][::-1] + string[26:][::-1])[string.index(i)] if i in string else i for i in message)
"""
U.S. government officials have disputed criticisms of PRISM in the Guardian and Washington Post articles and have defended the program, asserting that it cannot be used on domestic targets without a warrant, that it has helped to prevent acts of terrorism, and that it receives independent oversight from the federal government's executive, judicial and legislative branches.
F.H. tlevimnvmg luurxrzoh szev wrhkfgvw xirgrxrhnh lu KIRHN rm gsv Tfziwrzm zmw Dzhsrmtglm Klhg zigrxovh zmw szev wvuvmwvw gsv kiltizn, zhhvigrmt gszg rg xzmmlg yv fhvw lm wlnvhgrx gzitvgh drgslfg z dziizmg, gszg rg szh svokvw gl kivevmg zxgh lu gviilirhn, zmw gszg rg ivxvrevh rmwvkvmwvmg levihrtsg uiln gsv uvwvizo tlevimnvmg'h vcvxfgrev, qfwrxrzo zmw ovtrhozgrev yizmxsvh.
"""
def CaesarCryptography(key=None):
    if key is None:
        key = randrange(26) + 1
    else:
        key = int(key)
    a, b = [ord(i) for i in input()], []
    for i in a:
        if 96 < i < 123:
            b.append((i + key - 97) % 26 + 97)
        elif 64 < i < 91:
            b.append((i + key - 65) % 26 + 65)
        else:
            b.append(i)
    return ''.join(chr(i) for i in b)
def word_for_key(message: str, key_word: str):
    if len(key_word) < len(message):
        for i in range(len(message) - len(key_word)):
            key_word += key_word[i]
    a = tuple(ord(i) for i in message)
    b = []
    for i in range(len(a)):
        if 96 < a[i] < 123:
            b.append((a[i] + ord(key_word[i].lower()) - 193) % 26 + 97)
        elif 64 < a[i] < 91:
            b.append((a[i] + ord(key_word[i].upper()) - 129) % 26 + 65)
        else:
            b.append(a[i])
    return ''.join(chr(i) for i in b)