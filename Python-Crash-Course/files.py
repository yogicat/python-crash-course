# open file (or create one)
myFile = open('text.txt', 'w')

# get file info
print(myFile.name)
print(myFile.closed)
print(myFile.mode)

# write
myFile.write('I love Python!')
myFile.write(' and Javascript')
myFile.close()

# append
myFile = open('text.txt', 'a')
myFile.write(' I also like Ruby')
myFile.close()

# read
myFile = open('text.txt', 'r+')
text = myFile.read(100)
print(text)
