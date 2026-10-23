import os
with open("file_handling_data.txt","x")as f:
    f.write("\nFile Created")
    f.write("\nFile Opened")
    f.write("\nFile Data Written")
    f.write("\nFile Data Read")
with open("file_handling_data.txt","r")as f:
    print(f.read())
print("File Closed")
os.remove("file_handling_data.txt")
print("File Deleted")

