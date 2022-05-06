import os
import re

# Inititalize variables
orig_path = input("Enter origin file path: ")
while(not os.path.exists(orig_path)):
    orig_path = input("Invlaid path. Enter origin file path: ")
dest_path = input("Enter destination file path: ")
count = 0

# Create list of files at origin
files = os.listdir(orig_path)

# Change filename of files that ends with "_R.JPG"
for file in files:
    if re.search(".*_R.JPG$", file):
        os.rename(os.path.join(orig_path,file), 
            os.path.join(dest_path,file))
        count += 1

# Print confirmation of files renamed
print (f"%d files renamed and moved" %count)