import re

with open('encrypted_msgs.txt',"r") as myfile:
    data = myfile.read().split("\n")

counter = 0    
for line in data:
    targets = re.compile(r'([0-9]+)-([0-9]+)\s([a-z]):\s([a-z]+)')
    match = targets.match(line)
    #match regex to each group, ( in parentheses )
    if match:
        min_t = match.group(1)
        max_t = match.group(2)
        char_t = match.group(3)
        encrypt_t = match.group(4)
    
    if encrypt_t.count(char_t) < int(min_t) or encrypt_t.count(char_t) > int(max_t):
        counter+=1
        print(counter, min_t,max_t,char_t,encrypt_t)
    