#Made by Johan "Namastez" Lundgren
#Dependencies: N/A
#Python3
#A simple morse encode/decoder


morse_alphabet = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',
               'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
               'M':'--', 'N':'-.','O':'---','P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...',
               'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', '0':'-----',
               '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....',
               '7':'--...', '8':'---..', '9':'----.'}


def encrypt_morse(string):
    cipher = '' #Make an empty string, where the letters will be added
    for letter in string:
        if letter != ' ': #if not a blankspace
            cipher += morse_alphabet[letter] + ' ' #adding the value for letter if not blankspace
        else:
            cipher += ' ' #Adding a blankspace at the end of the cipher
    return cipher


def decrypt_morse(string):
    string += ' ' #adding a space at the end of the string
    decipher = ''
    text = ''
    for letter in string: #Go through each letter in the message
        if (letter != ' '): #If letter is not a blankspace
            i=0
            text += letter #add the letter to a variable
        else: #if there is a space
            i += 1 #Set to 1, which is a new char
            if i == 2: #If 2: new word
                decipher += ' ' #Adding space to seperate words
            else:
                #Go through the keys (by the values)
                decipher += list(morse_alphabet.keys())[list(morse_alphabet.values()).index(text)]
                text = ''
    return decipher



print(decrypt_morse('- . ... - .----'))
print(encrypt_morse('TEST2 HERE'))