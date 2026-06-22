menu_input = 99

def display_menu():
    print(" ")
    print("--------------------------------")
    print("||      Golden Pi OS v1       ||")
    print("--------------------------------")
    print(" ")
    print(" ")
    print("1: New study session")
    print("2: Load Memory")
    print("3: Search Memory")
    print("4: View Progress")
    print("5: Settings")
    print("0: Exit")
    print("")
while menu_input !=0 :
    display_menu()
    try :
        menu_input = int(input("Enter your choice:  "))
                
    except ValueError:
        print("Please input a number")
        continue
    
            

    if menu_input == 1 :
        print ("Coming soon")
        print(" ")
    
    elif menu_input == 2:
        print ("Coming soon")
        print(" ")

    elif menu_input == 3:
        print ("Coming soon")
        print(" ")

    elif menu_input == 4:
        print ("Coming soon")
        print(" ")

    elif menu_input == 5:
        print ("Coming soon")
        print(" ")
    
    elif menu_input == 0:
        print("Thank You for using Golden Pi OS")
        print("")
    
    else :
        print ("Invalid input, try a valid one according to the menu provided(1,2,3,4,5,0)")
        print(" ")
    