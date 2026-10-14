# ###################################################################
# Shift encryption
# ###################################################################

# this is (I'm pretty sure) like exactly an assignment I had in CSCI101, so it'll be good for you to do to learn

# create a string of the alphabet (I chose to do this in lowercase)
alphabet = "abcdefghijklmnopqrstuvwxyz"

# make an encrypt function
def encrypt(message, shift):
    # we will concatenate each letter as we encrypt it
    result = ""

    # for each character in a given message
    for char in message:
        # make it lowercase because I made my alphabet string lowercase letters
        # and A does not equal a (they have different ASCII values, but you don't necessarily need to know that)
        lower_char = char.lower()

        # if the character is in the alphabet
        if lower_char in alphabet:
            # you can use index to get the position in a string of a spacific character
            old_index = alphabet.index(lower_char)
            # use modulus (% in Python) to shift the index to the new index
            new_index = (old_index + shift) % 26

            # now that you have the new index, get the character at that index
            new_char = alphabet[new_index]

            # if the character was originally uppercase, make it uppercase again
            if char.isupper():
                new_char = new_char.upper()

            # concatenate the character to the result
            result += new_char

        # else the character is something like a space or apostrophe, so we will just add it
        else:
            result += char

    # return the result
    return result

# decrypt is just encrypting in the opposite direction
def decrypt(message, shift):
    return encrypt(message, -shift)

# get the secret message and encryption shift
message = input("Enter a secret message: ")
shift = int(input("Enter shift amount: "))

# encrypt and decrypt it
encrypted = encrypt(message, shift)
decrypted = decrypt(encrypted, shift)

# print the encryption and decryption
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)