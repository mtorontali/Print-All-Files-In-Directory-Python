# Matthew Torontali

import glob

# set list to all files in directory
list = glob.glob("/Users/USERNAME/testfolder/*")

# write list to file line by line
with open('dirContents.txt', 'w') as file:
    file.writelines("%s \n" % line for line in list)
