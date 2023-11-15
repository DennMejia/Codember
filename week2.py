
with open('message_02.txt',"r") as myfile:
    data = list(myfile.read())

value=0

for symbol in data:
    
    if symbol == '#':
        value += 1
    if symbol == '@':
        value -= 1
    if symbol == '*':
        value *= value
    if symbol == '&':
        print(value, end='')


