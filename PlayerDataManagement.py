import os
os.system("")

#Defining variables
File_Location = '';
List_Of_Tuple = []

#function to convert string to tuple.
#returing a created tuple usingg .split() to split every string after a space
#calling tuple creates a tuple
def Tuple_creation(x_string): return tuple(x_string.split())
    
  
#function to convert a tuple to a string  
#using .format to sort out the arrangement of the tuple( first-name/last-name/team/position ). 
#the * before x_tuple splits the tuple so it can be accessable.
# "|" is to creat a border like table
# ":<" this is print all the string to the left.
def String_Creation(x_tuple): return(ColourBlue(UnderLine(" {2:<15} │ {3:<15} │ £{4:<10} │ {1:<15} │ {0:<15}".format(*x_tuple).upper())))
    
#this is used to clear the screen, so it wont be messy.
def clear_screen(): os.system('cls')    
#this is used to change text styling using ANSIR
def ColourRed(Input): return("\033[91m{}\033[00m" .format(Input))
def ColourBlue(Input): return("\033[34m{}\033[00m" .format(Input))
def ColourPurple(Input): return("\033[95m{}\033[00m" .format(Input))
def UnderLine(Input): return("\033[4m{}\033[00m" .format(Input))
def GreyBG(Input): return("\033[7m{}\033[00m" .format(Input))
def InputChange(Input):
    x = input(ColourPurple(Input)+"\033[100m")
    Reset()
    return x
def Heading(Option):
    if(Option == 1):
        #gives a grey background to the table's heading
        print(UnderLine(GreyBG(" {0:<15} │ {1:<15} │ {2:<10}  │ {3:<15} │ {4:<15}".format("FIRST NAME","LAST NAME", "SALARY", "POSITION", "TEAM"))))
    elif(Option == 2):
        print(UnderLine(GreyBG(" {0:<15} │ {1:<15}".format("FIRST NAME","LAST NAME"))))
def Reset(): print("\033[00m")


try:
    #open(name, mode) is used to open a file amd r is used just to read the file.
    File_Location = open(InputChange("PLEASE TYPE IN FILE'S NAME: "), "r")
    #File_Location = open("TEST.txt", "r")
    #this is used to print a border like table
    Heading(1)
    #for loop is used to read each line in the text file
    for Lines_In_File in File_Location:
        #every line is read and a copy is saved into a list while it also calls the two defined functions to convert each line into tuples and them strings.
        print(String_Creation(Tuple_creation(Lines_In_File)))
        List_Of_Tuple.append(Tuple_creation(Lines_In_File))
    #while loop to keep repeating options for users
    while(True):
    
        #list of avaiable options
        print(ColourPurple("\n(1) SEARCH LASTNAME TO DISPLAY FULL DETAILS OF THE PLAYER."))
        print(ColourPurple("(2) SEARCH SALARY RANGE TO DISPLAY FULL DETAILS OF PLAYERS WITHIN THE RANGE"))
        print(ColourPurple("(3) SEARCH TEAM NAME TO DISPLAY FIRST AND LAST NAMES OF ALL PLAYERS"))
        print(ColourPurple("(4) SEARCH POSITION AND TEAM TO DISPLAY FULL DETAILS OF PLAYER"))
        print(ColourPurple("(5) SEARCH SALARY RANGE AND POSITION TO DISPLAY FULL DETAILS OF PLAYERS"))
        print(ColourPurple("(6) PROVIDE FULL DETAILS OF PLAYER TO ADD INTO THE LIST"))
        print(ColourPurple("(7) QUIT"))
        
        #user input to select an options
        #if statements is used to direct the user's input to the selected option.
        User_Number_Input = int(InputChange("\nWHAT NUMBER WOULD YOU LIKE TO PICK? "))
        #clearing previous outputs and inputs
        clear_screen()
        if(User_Number_Input == 1):
        
            Last_Name_Input = InputChange("PLEASE TYPE IN PLAYER'S LASTNAME: ")
            Heading(1)
            #If not checks if the result is empty and prints no result if no result is found
            #Enumerate stores the values and this loop is used to get the results of the check using the if statement.
            if not [print(String_Creation(Tuples_In_List)) for i, Tuples_In_List in enumerate(List_Of_Tuple) if Tuples_In_List[3].lower() == Last_Name_Input]: print(ColourRed(" NO RESULTS FOUND!!!"))

        elif(User_Number_Input == 2):
                    
            #accquiring user input and using .replace to remove any , found in the input so it can be compare using int.
            User_Min_Range = int(InputChange("PLEASE TYPE IN MINIMUN SALARY RANGE TO SEARCH: ").replace(",",""))
            User_Max_Range = int(InputChange("PLEASE TYPE IN MAXIMUN SALARY RANGE TO SEARCH: ").replace(",",""))
            Heading(1)            
            if not [print(String_Creation(Tuples_In_List)) for i, Tuples_In_List in enumerate(List_Of_Tuple) if int(Tuples_In_List[4].replace(",","")) >= User_Min_Range and  int(Tuples_In_List[4].replace(",","")) <= User_Max_Range]: print(ColourRed(" NO RESULTS FOUND!!!"))

        elif(User_Number_Input == 3):
    
            #.lower() is used to compare the values against each other so there's no issues with Capitals.
            User_Team_Input = InputChange("PLEASE TYPE IN TEAM'S NAME: ").lower()
            Heading(2)
            if not [print(ColourBlue(UnderLine(" {2:<15} │ {3:<15}".format(*Tuples_In_List)))) for i, Tuples_In_List in enumerate(List_Of_Tuple) if Tuples_In_List[0].lower() == User_Team_Input]: print(ColourRed(" NO RESULTS FOUND!!!"))

        elif(User_Number_Input == 4):
        
            User_Position_Input = InputChange("PLEASE TYPE IN POSITION: ").lower()
            User_Team_Input = InputChange("PLEASE TYPE IN TEAM'S NAME: ").lower()
            Heading(1)            
            if not [print(String_Creation(Tuples_In_List)) for i, Tuples_In_List in enumerate(List_Of_Tuple) if Tuples_In_List[0].lower() == User_Team_Input and Tuples_In_List[1].lower()== User_Position_Input]: print(ColourRed(" NO RESULTS FOUND!!!"))
  
        elif(User_Number_Input == 5):
        
            User_Min_Range = int(InputChange("PLEASE TYPE IN MINIMUN SALARY RANGE TO SEARCH: ").replace(",",""))
            User_Max_Range = int(InputChange("PLEASE TYPE IN MAXIMUN SALARY RANGE TO SEARCH: ").replace(",",""))
            User_Position_Input =InputChange("PLEASE TYPE IN POSITION: ").lower()
            Heading(1)
            #this is used to sort out the list in ascending order of the salary.
            List_Of_Tuple.sort( key=lambda x:int(x[4].replace(",","")) )            
            if not [print(String_Creation(Tuples_In_List)) for i, Tuples_In_List in enumerate(List_Of_Tuple) if int(Tuples_In_List[4].replace(",","")) >= User_Min_Range and  int(Tuples_In_List[4].replace(",","")) <= User_Max_Range and Tuples_In_List[1].lower()== User_Position_Input ]: print(ColourRed(" NO RESULTS FOUND!!!"))
  
        elif(User_Number_Input == 6):
        
            #.append is used to add data into the list
            #Tuple_creation function is called to convert the input to tuples.
            List_Of_Tuple.append(Tuple_creation("{0} {1} {2} {3} {4}".format(InputChange("PLEASE TYPE IN PLAYER'S TEAM: "),InputChange("PLEASE TYPE IN PLAYER'S POSITION: "),InputChange("PLEASE TYPE IN PLAYER'S FIRSTNAME: "),InputChange("PLEASE TYPE IN PLAYER'S LASTNAME: "),InputChange("PLEASE TYPE IN PLAYER'S SALARY: "))))
            #Shows user details has been added
            Heading(1)   
            for Tuples_In_List in List_Of_Tuple:
                print(String_Creation(Tuples_In_List))
                
        elif(User_Number_Input == 7):
            #break is called to break the loop
            break
            
        else:
            #prints this in case any other value is entered instead on ending loop
            print(ColourRed("UNKNOWN  value!!!"))
        
#THIS is used to catch and error and prints a message to the user.
except Exception as e:
    Reset()
    print(ColourRed("AN ERROR HAS OCCURED AND PROGRAM HAS BEEN TERMINATED. PLEASE RESTART PROGRAM.\n"+str(e)))
    




    