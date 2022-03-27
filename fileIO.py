#Read a file in Python
f = open('inputFile.txt', 'r')

#Write a file in python
passFile = open("PassFile.txt", 'w')
failFile = open("FailFile.txt", 'w')

#Now to check who passed and who failed, and count

for line in f:

    line_split = line.split() #this functions split the line at white space(blank)
    if line_split[2] == "P":
        passFile.write(line)
    else:
        failFile.write(line)

#close the file to prevent unforseen consequences
f.close()
passFile.close()
failFile.close()