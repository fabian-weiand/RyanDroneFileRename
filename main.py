import os
import re

# Inititalize variables
org_path = (r"C:\Users\Fabian\OneDrive\Documents\Projects\RyanDroneFileRename\30Apr2022")
dest_path = (r"C:\Users\Fabian\OneDrive\Documents\Projects\RyanDroneFileRename\30Apr2022_R")
count = 0

# Create list of files at origin
files = os.listdir(org_path)

# Change filename of files that start with "geeks"
for file in files:
    if re.search(".*_R.JPG$", file):
        os.rename(os.path.join(org_path,file), 
            os.path.join(dest_path,file))
        count += 1

# Print confirmation of files renamed
print (f"%d files renamed and moved" %count)