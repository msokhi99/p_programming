"""
Opening a file and displaying its contents.
Another method is as follows but the one shown 
with the "with" method is recommend. 

file_one=open("file_name.extension")
contents=file_one.read()
print(contents)
file_one.close()
"""

# with open("test_file.txt") as file_one:
#     contents=file_one.read()
#     print(contents)

"""
Writing to a file. By default the file mode is 
"read only". If we want to remove old text and add 
new text, we can change the mode to "w". If, we 
want to add to existing text, we can change the mode
to "a".

If the file name does not exist and file is on "w" mode
then compiler will create a new file with that name. This
only works if the file is in "w" mode.
"""

# with open("test_file.txt",mode="w") as file_one:
#     file_one.write("New Text")

# with open("test_file.txt",mode="a") as file_one:
#     file_one.write("\nHello")

# Challenge 1: 

# with open("/Users/bobby/OneDrive/Desktop/test_file.txt") as file_one:
#     contents=file_one.read()
#     print(contents)

# Challenge 2:

with open("../../../Desktop/test_file.txt") as file_one:
    contents=file_one.read()
    print(contents)
