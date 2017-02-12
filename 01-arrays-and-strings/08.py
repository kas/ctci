# assume you have a method isSubstring which checks if one word is a substring of another. given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only 1 call to isSubstring ("waterbottle" is a rotation of "erbottlewat")

S1 = 'erbottlewat'
S2 = 'waterbottle'

def is_rotation(s1, s2):
    s1s1 = s1 + s1 # erbottlewaterbottlewat
    s2_is_rotation = False

    if len(s1) != len(s2): # if lengths not same, can't be rotation
        pass
    elif s2 in s1s1: # waterbottle is in erbottlewaterbottlewat
        s2_is_rotation = True

    return s2_is_rotation

print(is_rotation(S1, S2))
