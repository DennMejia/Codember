from collections import defaultdict

#read in text file and separate by spaces
#data will be an array
with open('message_01.txt',"r") as myfile:
    data = myfile.read().split(" ")

#initialize defaultdict and count the number of times each word appears
d = defaultdict(int)
for i in data:
    d[i] += 1

#print the words and their counts
for k,v in d.items():
    print(f'{k}{v}',end='')
