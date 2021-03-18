import string

shift = 3
text = 'hello'
lower_chars = list(string.ascii_lowercase)
upper_chars = list(string.ascii_uppercase)


def mapChars(charset):

    mappedChars = {}
    for charIndex in range(len(charset)):
        key = charset[charIndex]
        value = charset[(charIndex + shift) % 26]
        mappedChars[key] = value
    return mappedChars


cipheredLower = mapChars(lower_chars)
cipheredUpper = mapChars(upper_chars)

cipheredAllChars = {**cipheredLower, **cipheredUpper}

print(cipheredAllChars)