# The Caesar cipher program allows you to encrypt and decrypt a message

Requirements: Python 3

# Program:
- at the beginning asks for a sentence to be encrypted
- asks if it should take into account Polish characters, i.e. ź
- encrypts the string of characters by shifting each character by three letters in our alphabet to the right <br>
e.g. for a it will be d (without polish characters), c (including polish characters)
- after rearranging all characters, it prints the encrypted message
- asks if we want to try again
- if not, ends the program
- if so, asks if we want to encrypt the message, if we type n, the program will start decrypting
- decryption is a reverse action to encryption
which means that this time we go left with the characters, being able to take into account polish characters or not
