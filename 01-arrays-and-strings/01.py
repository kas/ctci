# make algorithm to determine if str has all unique chars

def has_unique_chars(string):
    unique = True
    prev_chars = []

    for char in string:
        if not prev_chars:
            prev_chars.append(char)
        elif char in prev_chars:
            unique = False
            break
        else:
            prev_chars.append(char)

    return unique

def has_unique_chars_no_ds(string):
    for char in string:
        found = 0
        for other_char in string:
            if (char == other_char):
                found += 1
                if (found >= 2):
                    return False
    return True

string = input()

unique = has_unique_chars(string)
print('Using data structures:', unique)

unique = has_unique_chars_no_ds(string)
print('No data structures:', unique)
