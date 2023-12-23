# readline function reads only one line from the program , the more lines are the more readline function to be used
f = open ('sample.txt', 'r')
# reads first line 
data = f.readline()
print (data)
# reads second line
data = f.readline()
print (data)
# reads third line
data = f.readline()
print (data)
# reads fourth line
data = f.readline()
print (data)
# closes the program
f.close()

