alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m",
    "n","o","p","q","r","s","t","u","v","w","x","y","z"]

def encrypt(plain_text,shift_amount):
    cipher = ""
    for i in plain_text:
        if i in alphabet:
            position = alphabet.index(i)
            new_position = position + shift_amount
            newl = alphabet[new_position]
            cipher += newl
        else:
            cipher+=i
    print(f"the encoded text is {cipher}")    

def decrypt(ptext,ashift):
    plaintext=""
    for j in ptext:
        if j in alphabet:
            pose = alphabet.index(j)
            new_pose = pose - ashift
            newll = alphabet[new_pose]
            plaintext+=newll
        else:
            plaintext+=j
    print(f"your decoded message is {plaintext}")
    y=True
    while y:
        direction = input("type e for encode or d for decode : \n").lower()
        text = input("type ur message \n").lower()
        shift = int(input("type ur shift number : \n"))

        shift = shift%26

        if direction=='e':
            encrypt(plain_text=text,shift_amount=shift)
        elif direction=='d':
            decrypt(ptext=text,ashift=shift)
        restart = input("do u want to encode or decode again choose yes or no").lower()
        if restart == 'no':
            y=False