import re

with open('message_04.txt',"r") as myfile:
    data = myfile.read().split("\n")

count = 0
for line in data:
    target = re.compile(r'([a-zA-Z0-9]+)-([a-zA-Z0-9]+)')
    match = target.match(line)

    if match:
        name = match.group(1)
        checksum = match.group(2)
    correct_checksum = ""
    
    for chars in name:
        #print(chars)
        if name.count(chars) == 1:
            
            correct_checksum += chars
        
    if correct_checksum == checksum:
        count+=1
        print(count,name,checksum,correct_checksum)