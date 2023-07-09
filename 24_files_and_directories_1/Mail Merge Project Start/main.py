#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# with open('./Input/Letters/starting_letter.txt','r') as data:
#     letter = data.read()

# print(letter)
# letter = letter.replace('[name]','test')

# with open('./Output/ReadyToSend/letter_to_test.txt','w') as file_to_send:
#     file_to_send.write(letter)

with open('./Input/Names/invited_names.txt','r') as data:
    new_names = data.readlines()
names = [x.strip() for x in new_names]

for name in names:
    with open('./Input/Letters/starting_letter.txt','r') as data:
        letter = data.read()
    letter = letter.replace('[name]',name)
    with open(f'./Output/ReadyToSend/letter_for_{name}.txt','w') as file_to_send:
        file_to_send.write(letter)