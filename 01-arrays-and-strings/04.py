# write a method to replace all spaces in a string with '%20'. assume string has sufficient space at the end to hold additional characters, and that you are given the true length of the str.

def replace(str):
    return str.replace(' ', '%20')

print(replace('Hello, World!'))
