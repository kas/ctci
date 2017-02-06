# given 2 strings, write a method to decide if one is a permutation of the other

def is_permutation(string_a, string_b):
    if (string_a == string_b):
        return False

    hash_a = {}
    hash_b = {}

    for char in string_a:
        if (char in hash_a):
            hash_a[char] += 1
        else:
            hash_a[char] = 1

    for char in string_b:
        if (char in hash_b):
            hash_b[char] += 1
        else:
            hash_b[char] = 1


    if (hash_a == hash_b):
        return True
    else:
        return False

string_a = input()
string_b = input()

print(is_permutation(string_a, string_b))
