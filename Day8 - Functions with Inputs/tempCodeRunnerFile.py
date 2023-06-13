function = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text= input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

decrypt(text,shift)