alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    cipher_text = ""
    if encode_or_decode == "encode":
        for letter in original_text:
            if letter in alphabet:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet)
                cipher_text += alphabet[shifted_position]
            else:
                cipher_text += letter    
        print(f"Here is the encoded result: {cipher_text}")
    
    if encode_or_decode == "decode":
        for letter in original_text:
            if letter in alphabet:
                shifted_position = alphabet.index(letter) - shift_amount
                cipher_text += alphabet[shifted_position]
            else:
                cipher_text += letter            
        print(f"Here is the decoded result: {cipher_text}")        

continue_to_encrption = True
while continue_to_encrption:
     
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n" ).lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
     
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n" ).lower()
    if restart == "no":
        continue_to_encrption = False
        print("Goodbye")