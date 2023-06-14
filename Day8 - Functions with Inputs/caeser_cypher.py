alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
reverse_alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
reverse_alphabet.reverse()



def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == 'decode':
            shift_amount = shift_amount *  -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position+shift_amount
            end_text += alphabet[new_position]
        else:
             end_text += char

    print(f"Here's your {cipher_direction}d message: {end_text}")
    
def cipher():
     val = True
     while val:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
        text= input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        caesar(text,shift,direction)
        continue_ = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
        if continue_ == 'no':
             val = False
             print("See you next time")

cipher()




# OLD SEPARETED FUNCTIONS
# def encrypt(message,shift_amount):
#       encrypted = ""
#       for letter in message:
#         position = alphabet.index(letter)
#         encrypted += alphabet[position+shift_amount]
#       print(f"Here's your encrypted message: {encrypted}")
    
# def decrypt(message,shift_amount):
#     decrypted = ""
#     for letter in message:
#         position = reverse_alphabet.index(letter)
#         decrypted += reverse_alphabet[position+shift_amount]
#     print(f"Here's your decrypted message: {decrypted}")







# if direction == 'encode':
#     encrypt(message = text,shift_amount=shift)
# elif direction == 'decode':
#     decrypt(message=text,shift_amount=shift)





