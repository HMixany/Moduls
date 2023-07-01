message = input("Enter a message: ")
offset = int(input("Enter the offset: "))
encoded_message = ""
for ch in message:
    if ch.isalpha():
        if ch.isupper():
            ascii_offset = 65
        else:
            ascii_offset = 97

        pos = ord(ch) - ascii_offset
        pos = (pos + offset) % 26
        encoded_message += chr(pos + ascii_offset)
    else:
        encoded_message += ch
print(encoded_message)