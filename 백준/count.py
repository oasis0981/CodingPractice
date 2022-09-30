f = open("C:/StudentFile/studata.txt", 'r')
line = f.read()
f.close()

email = line.split(',')
print(len(email))