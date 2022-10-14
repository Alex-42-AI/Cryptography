"""
00 1054560
01 342732000
02 47297016000
03 3641870232000
04 172988836020000
05 5293458382212000
06 105869167644240000
07 1376299179375120000
08 11354468229844740000
09 56772341149223700000
10 158962555217826360000
11 216767120751581400000
12 108383560375790700000
13 8337196951983900000

from math import factorial
def f(_i: int):
    return 60 * 26 ** 3 * factorial(26) // (factorial(26 - 2 * _i) * factorial(_i) * 2 ** _i)
def g(_i: int):
    return 26 ** 2 * factorial(26) ** 5 // (2 ** (13 + _i) * factorial(13) * (factorial(26 - 2 * _i) * factorial(_i)))
print(f(10), f(11), g(10), g(11), sum(map(g, range(14))), sep='\n')

                 f(10) =  158962555217826360000
                 f(11) =  216767120751581400000
                 g(10) =  52841615182541934867380880379974902806941642035152636578099608189263918507485623746560000000000000000000000000
                 g(11) =  72056747976193547546428473245420322009465875502480868061044920258087161601116759654400000000000000000000000000
sum(map(g, range(14))) = 186839071108157384996636441415047152219471994297031498823429747361328478992481746954485760000000000000000000000
"""
class Pair:
    def __init__(self, fst: str, snd: str):
        if fst == snd:
            raise ValueError
        self.first = fst
        self.second = snd
    def other(self, _l):
        if _l in (self.first, self.second):
            return [self.first, self.second][_l == self.first]
    def __contains__(self, item):
        return item in (self.first, self.second)
    def __eq__(self, other):
        return self.first in other and self.second in other
    def __str__(self):
        return self.first + '-' + self.second
    def __repr__(self):
        return str(self)
class Rotor:
    def __init__(self, value: dict):
        self.__rotor = value
    def copy(self):
        return Rotor(self.__rotor.copy())
    def keys(self):
        return self.__rotor.keys()
    def values(self):
        return self.__rotor.values()
    def items(self):
        return self.__rotor.items()
    def rotate(self):
        res_values = list(self.values())
        res_values = res_values[1:] + [res_values[0]]
        self.__rotor = Rotor(dict(zip(self.keys(), res_values)))
    def __len__(self):
        return len(self.__rotor)
    def __getitem__(self, item):
        return self.__rotor[item]
    def __setitem__(self, key, value):
        self.__rotor[key] = value
        return value
    def __eq__(self, other):
        if len(self) != len(other):
            return False
        this_values = list(self.values())
        other_values = list(other.values())
        for _ in range(len(self)):
            if this_values == other_values:
                return True
            this_values = this_values[1:] + [this_values[0]]
        return False
    def __str__(self):
        return str(self.__rotor)
    def __repr__(self):
        return repr(self.__rotor)
def rotated(rotor: Rotor):
    _rotor = rotor.copy()
    res_values = list(_rotor.values())
    res_values = res_values[1:] + [res_values[0]]
    return Rotor(dict(zip(_rotor.keys(), res_values)))
rotor1 = Rotor({'a': 'v', 'b': 'y', 'c': 't', 'd': 'a', 'e': 'b', 'f': 'h', 'g': 'd', 'h': 'q', 'i': 'o', 'j': 'j', 'k': 'l', 'l': 's', 'm': 'u', 'n': 'e', 'o': 'p', 'p': 'f', 'q': 'r', 'r': 'i', 's': 'w', 't': 'c', 'u': 'x', 'v': 'n', 'w': 'g', 'x': 'm', 'y': 'k', 'z': 'z'})
rotor2 = Rotor({'a': 'f', 'b': 'w', 'c': 'o', 'd': 'i', 'e': 'p', 'f': 'h', 'g': 'm', 'h': 'x', 'i': 'k', 'j': 'n', 'k': 'u', 'l': 'r', 'm': 's', 'n': 'c', 'o': 'q', 'p': 'e', 'q': 'a', 'r': 'g', 's': 'l', 't': 'v', 'u': 'd', 'v': 'b', 'w': 't', 'x': 'j', 'y': 'z', 'z': 'y'})
rotor3 = Rotor({'a': 'v', 'b': 'k', 'c': 'n', 'd': 'h', 'e': 'd', 'f': 'f', 'g': 'b', 'h': 'u', 'i': 'l', 'j': 'c', 'k': 'q', 'l': 'p', 'm': 'r', 'n': 'j', 'o': 'z', 'p': 'e', 'q': 'm', 'r': 'o', 's': 'g', 't': 'x', 'u': 'i', 'v': 't', 'w': 's', 'x': 'a', 'y': 'y', 'z': 'w'})
rotor4 = Rotor({'a': 'x', 'b': 't', 'c': 'k', 'd': 'a', 'e': 'z', 'f': 's', 'g': 'n', 'h': 'y', 'i': 'o', 'j': 'l', 'k': 'w', 'l': 'q', 'm': 'i', 'n': 'f', 'o': 'u', 'p': 'g', 'q': 'd', 'r': 'p', 's': 'b', 't': 'r', 'u': 'm', 'v': 'j', 'w': 'c', 'x': 'h', 'y': 'e', 'z': 'v'})
rotor5 = Rotor({'a': 'l', 'b': 'm', 'c': 'e', 'd': 'o', 'e': 'i', 'f': 'p', 'g': 'f', 'h': 'g', 'i': 'y', 'j': 's', 'k': 'b', 'l': 'r', 'm': 'k', 'n': 'h', 'o': 'j', 'p': 'u', 'q': 'd', 'r': 'q', 's': 'c', 't': 'v', 'u': 'a', 'v': 'n', 'w': 'x', 'x': 'w', 'y': 'z', 'z': 't'})
all_rotors = [rotor1, rotor2, rotor3, rotor4, rotor5]
reflector = [Pair('a', 'p'), Pair('h', 'l'), Pair('v', 'n'), Pair('s', 'z'), Pair('k', 'x'), Pair('e', 'b'), Pair('q', 'w'), Pair('j', 'm'), Pair('i', 'd'), Pair('o', 'c'), Pair('u', 'g'), Pair('t', 'f'), Pair('r', 'y')]
Plugboard = [Pair('n', 'e'), Pair('l', 't'), Pair('y', 's'), Pair('d', 'v'), Pair('q', 'h'), Pair('p', 'c'), Pair('k', 'o'), Pair('r', 'm'), Pair('u', 'i'), Pair('g', 'f')]
def encrypt(message: str, rotors: [Rotor, Rotor, Rotor], rotor1rotations: int, rotor2rotations: int, rotor3rotations: int, plugboard: [Pair]):
    for _ in range(rotor1rotations):
        rotors[0] = rotated(rotors[0])
    for _ in range(rotor2rotations):
        rotors[1] = rotated(rotors[1])
    for _ in range(rotor3rotations):
        rotors[2] = rotated(rotors[2])
    res, total = '', 0
    for l in message:
        if l.isalpha():
            l = l.lower()
            total += 1
            rotors[0] = rotated(rotors[0])
            if not total % 26:
                rotors[1] = rotated(rotors[1])
                if not total % 676:
                    rotors[2] = rotated(rotors[2])
            for p in plugboard:
                if l in p:
                    l = p.other(l)
                    break
            l = rotors[0][l]
            l = rotors[1][l]
            l = rotors[2][l]
            for p in reflector:
                if l in p:
                    l = p.other(l)
                    break
            l = list(rotors[2].keys())[list(rotors[2].values()).index(l)]
            l = list(rotors[1].keys())[list(rotors[1].values()).index(l)]
            l = list(rotors[0].keys())[list(rotors[0].values()).index(l)]
            for p in plugboard:
                if l in p:
                    l = p.other(l)
                    break
        res += l
    return res
if __name__ == "__main__":
    print(encrypt('testingencryptiondecryption', [rotor1, rotor2, rotor4], 1, 1, 2, Plugboard))
