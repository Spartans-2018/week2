#ASCII
list = [ord('a'), ord('b'), ord('A'), chr(100), chr(90)]
# print(list)

# A-Z >> 65-90
# a-z >> 97-122
def ceasar(message, shift_number):

    encrypted_cipher=[]
    for letter in message:
        encrypted_cipher.append(chr(ord(letter) + shift_number))
    
    return encrypted_cipher

print(ceasar("HelloZ", 3))

# ?? wrapping
# ?? join() 