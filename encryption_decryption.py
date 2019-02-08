alphabet="abcdefghijklmnopqrstuvwxyz"

key=int(input("enter the key 1-26"))

if(key>26 or key<0):
    print("invalid number")
    exit()

message=input("Please enter the message")
newMessage=""

for character in message:
    position=alphabet.find(character)
    newPosition=(position+key)%26
    newVar=alphabet[newPosition]
    newMessage+=newVar

print(newMessage)


alphabet="abcdefghijklmnopqrstuvwxyz"

key=int(input("enter the key"))

if(key>26 or key<0):
    print("Invalid Number")
    exit()
message=input("Please enter the message")
newMessage=""

for character in message:
    position=alphabet.find(character)
    newPosition=(position-key)%26
    newVar=alphabet[newPosition]
    newMessage+=newVar

print(newMessage)