
# Different modes or accesing files.....

# - 'r' open for reading (Default)
# - 'w' open for writing, truncating the file first (Meaning it will overwrite on the text is already wirtten in that file)
# - 'x' create a new file and open it for writing
# - 'a' open for writing. appending to the end of the file if it exists
# - 'b' binary mode
# - 't' text mode
# - '+' open a disk file for updating (reading and writing)



# what are the commands to read a file?

# data = f.read() [It reads the entire file]
# date = f.readline() [reads one line at a time]



# Example

f = open("test.py", "r")
data = f.read()
print(data)
f.close()


# Another Example

with open("test.py", "r") as f:
    data = f.read()
print(data)