alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
reverse_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
reverse_alphabet.reverse()

def encrypt(message,shift_amount):
    encrypted = ""
    for letter in message:
        position = alphabet.index(letter)
        encrypted += alphabet[position+shift_amount]
    print(encrypted)
    
def decrypt(message,shift_amount):
    decrypted = ""
    for letter in message:
        position = reverse_alphabet.index(letter)
        decrypted += reverse_alphabet[position+shift_amount]
    print(decrypted)





function = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text= input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
encrypt(text,shift)
decrypt(input('typ encrypted message here\n'),shift)

