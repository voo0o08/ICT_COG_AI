import os

os.mkdir("tmp")
os.chdir("tmp")

for x in range(26):
    fname = chr(ord('A')+x) + ".txt"
    ofile = open(fname, "w")
    ofile.close()
