def alphabet_position(letter):
    if letter.isupper():
        return (ord(letter)-65)       #convert char to integer using ASCII code
    else:
        return (ord(letter)-97)
def rotate_character(char,rot):
    pos = (alphabet_position(char)+rot)%26
    new_char = chr(pos+65)          #convert to char using the ASCII code
    if char.islower():              #save the case of the character being rotated
        new_char = new_char.lower()
    return new_char

def encrypt(text,rot):
    cipher = ''
    for i in text:
        if i.isalpha():             #If the character is  alpha then  rotate else leave it
            cipher += rotate_character(i,rot)
        else:
            cipher += i
    return cipher