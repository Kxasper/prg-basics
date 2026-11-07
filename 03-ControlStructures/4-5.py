#źle nie mam pojęcia jak to zrobić + angielski troche problem ale nie szczegolny
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    code=ord(char)
    new_code= code + 1
    encrypted_text+=(new_code)
    # add one to the character's code

    # replace new character code with its
    # corresponding character (use chr())
    
    # add encrypted character to encrypted text
    

print(plain_text)
print(encrypted_text)