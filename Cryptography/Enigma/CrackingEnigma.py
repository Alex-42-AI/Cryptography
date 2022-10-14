from itertools import permutations
from Personal.Cryptography.Enigma.Enigma import Pair, all_rotors, reflector, rotated, encrypt
def decrypt_civil_enigma(message: str, supposed_substring: str):
    for i in range(len(message) - len(supposed_substring) + 1):
        if all(supposed_substring[_] != message[i + _] for _ in range(len(supposed_substring))):
            for rotors in map(list, permutations(all_rotors, 3)):
                for rotor3rotations in range(26):
                    curr_rotor_2 = rotors[2].copy()
                    for rotor2rotations in range(26):
                        curr_rotor_1 = rotors[1].copy()
                        for rotor1rotations in range(26):
                            curr_rotor_0 = rotors[0].copy()
                            for _ in range(i):
                                curr_rotor_0 = rotated(curr_rotor_0)
                                if not (_ + 1) % 26:
                                    curr_rotor_1 = rotated(curr_rotor_1)
                                    if not (_ + 1) % 676:
                                        curr_rotor_2 = rotated(curr_rotor_2)
                            total, works = i, True
                            for j, l in enumerate(supposed_substring):
                                total += 1
                                curr_rotor_0.rotate()
                                if not total % 26:
                                    curr_rotor_1.rotate()
                                    if not total % 676:
                                        curr_rotor_2.rotate()
                                l = curr_rotor_0[l]
                                l = curr_rotor_1[l]
                                l = curr_rotor_2[l]
                                for p in reflector:
                                    if l in p:
                                        l = p.other(l)
                                        break
                                for k, v in curr_rotor_2.items():
                                    if l == v:
                                        l = k
                                        break
                                for k, v in curr_rotor_1.items():
                                    if l == v:
                                        l = k
                                        break
                                for k, v in curr_rotor_0.items():
                                    if l == v:
                                        l = k
                                        break
                                if l != message[i + j]:
                                    works = False
                                    break
                            if works:
                                yield f'{all_rotors.index(rotors[0]) + 1} {all_rotors.index(rotors[1]) + 1} {all_rotors.index(rotors[2]) + 1} | {rotor1rotations:02d} {rotor2rotations:02d} {rotor3rotations:02d} -> {encrypt(message, rotors.copy(), 0, 0, 0)}'
                            rotors[0] = rotated(rotors[0])
                        rotors[1] = rotated(rotors[1])
                    rotors[2] = rotated(rotors[2])
def decrypt_military_enigma(message: str, supposed_substring: str):
    def free(letter: str):
        for pair in pairs:
            if letter in pair:
                return False
        return letter not in singles
    start = supposed_substring[0]
    alphabet = ''.join('abcdefghijklmnopqrstuvwxyz'.split(start)) + ' '
    for i in range(len(message) - len(supposed_substring) + 1):
        if all(supposed_substring[_] != message[i + _] for _ in range(len(supposed_substring))):
            for rotors in map(list, permutations(all_rotors, 3)):
                for rotor3rotations in range(26):
                    curr_rotor_2 = rotors[2].copy()
                    for rotor2rotations in range(26):
                        curr_rotor_1 = rotors[1].copy()
                        for rotor1rotations in range(26):
                            curr_rotor_0 = rotors[0].copy()
                            for _ in range(i):
                                curr_rotor_0 = rotated(curr_rotor_0)
                                if not (_ + 1) % 26:
                                    curr_rotor_1 = rotated(curr_rotor_1)
                                    if not (_ + 1) % 676:
                                        curr_rotor_2 = rotated(curr_rotor_2)
                            poison_tree = []
                            total, works = i, True
                            for _l in alphabet:
                                curr_curr_rotor_0, curr_curr_rotor_1, curr_curr_rotor_2 = curr_rotor_0.copy(), curr_rotor_1.copy(), curr_rotor_2.copy()
                                pairs, singles = [], set()
                                if _l != ' ':
                                    if Pair(start, _l) in poison_tree:
                                        continue
                                    else:
                                        pairs.append(Pair(start, _l))
                                else:
                                    singles.add(start)
                                for j, l in enumerate(supposed_substring):
                                    total += 1
                                    curr_curr_rotor_0.rotate()
                                    if not total % 26:
                                        curr_curr_rotor_1.rotate()
                                        if not total % 676:
                                            curr_curr_rotor_2.rotate()
                                    for p in pairs:
                                        if l in p:
                                            l = p.other(l)
                                            break
                                    l = curr_curr_rotor_0[l]
                                    l = curr_curr_rotor_1[l]
                                    l = curr_curr_rotor_2[l]
                                    for p in reflector:
                                        if l in p:
                                            l = p.other(l)
                                            break
                                    for k, v in curr_curr_rotor_2.items():
                                        if l == v:
                                            l = k
                                            break
                                    for k, v in curr_curr_rotor_1.items():
                                        if l == v:
                                            l = k
                                            break
                                    for k, v in curr_curr_rotor_0.items():
                                        if l == v:
                                            l = k
                                            break
                                    if l != message[i + j]:
                                        if Pair(l, message[i + j]) not in pairs:
                                            if len(pairs) == 10 or Pair(l, message[i + j]) in poison_tree or {l, message[i + j]}.intersection(singles) or any(Pair(l, _) in pairs for _ in filter(lambda _l: _l != l, 'abcdefghijklmnopqrstuvwxyz')) or any(Pair(message[i + j], _) in pairs for _ in filter(lambda _l: _l != message[i + j], alphabet)):
                                                works = False
                                                poison_tree += list(filter(lambda _p: _p not in poison_tree, pairs + [Pair(l, message[i + j])]))
                                                break
                                            pairs.append(Pair(l, message[i + j]))
                                    elif len(singles) == 6:
                                        works = False
                                        poison_tree += list(filter(lambda _p: _p not in poison_tree, pairs + [Pair(l, message[i + j])]))
                                        break
                                    else:
                                        singles.add(l)
                                if works:
                                    yield f'{all_rotors.index(rotors[0]) + 1} {all_rotors.index(rotors[1]) + 1} {all_rotors.index(rotors[2]) + 1} | {rotor1rotations:02d} {rotor2rotations:02d} {rotor3rotations:02d} | {pairs} -> {encrypt(message, rotors.copy(), 0, 0, 0, pairs)}'
                            rotors[0] = rotated(rotors[0])
                        rotors[1] = rotated(rotors[1])
                    rotors[2] = rotated(rotors[2])
from time import time
item = decrypt_military_enigma('jmlcnfvzmzemfdoxhucgairbhjk', 'testingencryption')  # testingencryptiondecryption
t = time()
for el in item:
    print(el)
print(time() - t)
