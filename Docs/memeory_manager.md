This is how the memeory manager is gonna deal with the input

The input will be in json provided by the AI 

And this is the flow of it 



So this is how the project architecture is gonna flow :

1. AI give the input 
2. checks if there is a relative path subject/topic 
        2.1. If not found inform the user and ask for conformation for the creation 
        2.2. If found then proceed with the next step
3. The next step is to check whether all sections exists inside the subject/topic path
        3.1. If section found proceed 
        3.2. If not found then just create a new section
4. Checks whether the overwrite is True or False
        4.1. If True then copy the current contents in the section to a archive file and then use the write function to overwrite the file 
        4.2 If False then use the append function from file_manager
5. Give the user output of what all things were modified and in future (v2) we may even implement an undo function if needed .

If some error occurs aborth the mission and let the user know about the error. 