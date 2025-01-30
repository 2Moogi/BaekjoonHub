sen = input()
enc = ''
for char in sen:
    if 123 >ord(char)>109 or 77 < ord(char) <91:
        enc += chr(ord(char)-13)
    elif 110 > ord(char) > 96 or 64 < ord(char) < 78:
        enc += chr(ord(char)+13)
    else:
        enc += char
        
print(enc)
