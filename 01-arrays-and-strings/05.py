# write a method to perform basic string compression using the counts of repeated characters (aabcccccaaa => a2b1c5a3). if compressed string not smaller than original, return original string

def compress(string):
    letters_count = []

    current_char = None
    current_char_count = 0

    for i, char in enumerate(string):
        if current_char is None:
            current_char = char
        elif char == current_char:
            current_char_count += 1
        elif char != current_char:
            letters_count.append(current_char + str(current_char_count))
            current_char = char
            current_char_count = 1

        if i == (len(string) - 1):
            letters_count.append(current_char + str(current_char_count))

    compressed_string = ''.join(letters_count)

    if len(compressed_string) >= len(string):
        return string
    else:
        return compressed_string

print(compress('aabcccccaaa'))
