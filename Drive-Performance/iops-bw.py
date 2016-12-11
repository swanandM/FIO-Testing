#This python file reads all output files and parses IOPS and BW values from it.
#Creates 2 new files for each of them.

import re

file = open("iops.txt", "w")
file1 = open("bw.txt", "w")
string = "output"
string1 = ".txt"

for i in range (1,40):
 X=string+str(i)+string1
 hand = open(X)
 for line in hand:
    line = line.rstrip()

    if re.search('iops=', line) :
	line1=line.split("iops=",1)[1]
	line2=line1.split(",",1)[0]
	file.write(line2 +"\n")
	
    if re.search('bw=', line) :
	line1=line.split("bw=",1)[1]
	line2=line1.split(",",1)[0]
	file1.write(line2 +"\n")
