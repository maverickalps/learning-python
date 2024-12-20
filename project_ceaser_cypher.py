alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
if direction != "encode" and direction != "decode":
    print("Invalid input")
    exit()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# def encrypt(text, shift):
    # encrypted_text = ""
    # for letter in text:
    #     if letter in alphabets:
    #         position =alphabets.index(letter)
    #         new_position = position + shift 
    #         new_position %= len(alphabets)
    #         encrypted_text += alphabets[new_position]
            
    # print(f"The encoded text is {encrypted_text}")

# # def decrypt(text, shift):
#     encrypted_text = ""
#     for letter in text:
#         if letter in alphabets:
#             position =alphabets.index(letter)
#             new_position = position - shift 
#             new_position %= len(alphabets)
#             encrypted_text += alphabets[new_position]
            
#     print(f"The encoded text is {encrypted_text}")

def ceaser(text,shift,direction):
    crypted_text = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        if letter not in alphabets:
            crypted_text += letter
        else:
            position =alphabets.index(letter)
            new_position = position + shift 
            new_position %= len(alphabets)
            crypted_text += alphabets[new_position]
            
    print(f"The encoded text is {crypted_text}")

should_continue = True
while should_continue:
    ceaser(text,shift,direction)
    restart = input("Do you want to restart the program? Type 'yes' or 'no'").lower()
    if restart == "no":
        should_continue = False 
        print("Goodbye")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction != "encode" and direction != "decode":
        print("Invalid input")
        exit()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
