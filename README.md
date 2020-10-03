# How to print all files in a directory using Python3

```python
import glob

# Create list of all files in a directory and print them
list = glob.glob("/Users/USERNAME/testfolder/*")
print(list)
```

# Add files names to .txt files

```python
# Matthew Torontali

import glob

# set list to all files in directory
list = glob.glob("/Users/USERNAME/testfolder/*")

# write list to file line by line
with open('dirContents.txt', 'w') as file:
    file.writelines("%s \n" % line for line in list)
```