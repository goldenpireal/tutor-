from Scripts import file_manager



def display_menu():
    print(" ")
    print("--------------------------------")
    print("||      Golden Pi OS v1       ||")
    print("--------------------------------")
    print(" ")
    print(" ")
    print("1: New study session")
    print("2: Load Memory")
    print("3: View Progress")
    print("4: Settings")
    print("0: Exit")
    print("")



def input_menu():
    
    menu_input = -1
    display_menu()

    while menu_input > 4 or menu_input < 0 :

        try :
            menu_input = int(input("Enter your choice:  "))
                    
        except ValueError:
            print("Please input a number")
            print("\n")
            continue
        

        if menu_input > 4 or menu_input < 0:
            print ("Please input a valid option")
            print("\n")


    return menu_input



class SpecifiInput:
    
    #input_menu()

    def __init__(self, menu_input):
        self.menu_input = menu_input

    def NewStudySession():
        

        #this should first allow to input the data that is needed 
        #then should call the memory manager for sorting it 
        #the memory manager should contain the file_manager modules which will then sort everything
        
        pass


    def LoadMemory():
        
        #This should first display all the user data stored files
        #Should give the user the ability to select different files/ folders
        #Should enquire with the user what do they want - summary , the entire file , the file in the raw .json format 
        #It should call the fiile_manager to fetch the data for it and to scan through the files

        pass


    def ViewProgress():

        #This just displays the user progress over the selected time
        #The deisgning of this will be done later

        pass


    def Settings():

        #This will connect with all the user tweakable settings 

        pass



match input_menu():

    case 1:
        SpecifiInput.NewStudySession()
        
        print("Sucessfully loaded New Study session")
    
    case 2:
        SpecifiInput.LoadMemory()
        
        print("Sucessfully loaded New Study session")

    case 3:
        SpecifiInput.ViewProgress
        
        print("Sucessfully loaded New Study session")

    case 4:
        SpecifiInput.Settings()
        
        print("Sucessfully loaded New Study session")

    case 0:
        pass 





    