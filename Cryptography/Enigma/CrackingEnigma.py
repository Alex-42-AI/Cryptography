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
    def work_out_settings(current_substring: str, total: int, pairs=None, singles=None, poison_tree=None):
        if not current_substring:
            yield f'{all_rotors.index(rotors[0]) + 1} {all_rotors.index(rotors[1]) + 1} {all_rotors.index(rotors[2]) + 1} | {rotor1rotations:02d} {rotor2rotations:02d} {rotor3rotations:02d} | {pairs} | {singles} -> {military_encryption(message, rotors.copy(), 0, 0, 0, pairs)}'
        if poison_tree is None:
            poison_tree = []
        if singles is None:
            singles = set()
        if pairs is None:
            pairs = []
        def free(letter: str):
            for pair in pairs:
                if letter in pair:
                    return False
            return letter not in singles
        if free(current_substring[0]):
            for other in ''.join(alphabet.split(current_substring[0])) + ' ':
                _pairs, _singles = pairs.copy(), singles.copy()
                if other == ' ':
                    _singles.add(current_substring[0])
                else:
                    if not free(other):
                        continue
                    _pairs.append(Pair(current_substring[0], other))
                for _res in work_out_settings(supposed_substring, total, _pairs, _singles):
                    yield _res
            return
        total += 1
        curr_curr_rotor_0.rotate()
        if not total % 26:
            curr_curr_rotor_1.rotate()
            if not total % 676:
                curr_curr_rotor_2.rotate()
        l = current_substring[0]
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
        works = True
        if l != message[i]:
            if Pair(l, message[i]) not in pairs:
                if len(pairs) == 10 or Pair(l, message[i]) in poison_tree or not (free(l) and free(message[i])):
                    works = False
                    poison_tree += list(filter(lambda _p: _p not in poison_tree, pairs + [Pair(l, message[i])]))
                else:
                    pairs.append(Pair(l, message[i]))
        elif len(singles) == 6 or any(Pair(l, _) in pairs for _ in list(filter(lambda _l: _l != l, alphabet))):
            works = False
            poison_tree += list(filter(lambda _p: _p not in poison_tree, pairs))
        else:
            singles.add(l)
        if not works:
            return
        for _res in work_out_settings(current_substring[1:], total + 1, pairs, singles, poison_tree):
            yield _res
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
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
                            curr_curr_rotor_0, curr_curr_rotor_1, curr_curr_rotor_2 = curr_rotor_0.copy(), curr_rotor_1.copy(), curr_rotor_2.copy()
                            for res in work_out_settings(supposed_substring, i):
                                yield res
                            rotors[0] = rotated(rotors[0])
                        rotors[1] = rotated(rotors[1])
                    rotors[2] = rotated(rotors[2])
from time import time
item = decrypt_military_enigma('jmlcnfvzmzemfdoxhucgairbujk', 'testingencryption')  # testingencryptiondecryption
t = time()
for el in item:
    print(el)
print(time() - t)
