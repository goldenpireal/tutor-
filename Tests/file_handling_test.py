file_name = input ("Enter file name: ")
text_added = input ("Enter the new text: ")
file_name += ".md"

with open(file_name ,"w") as file:
    file.write(text_added)