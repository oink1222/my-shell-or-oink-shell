print("oink shell by jonathan ver 0.1 type help for the list of commands")
userName = "oink"
from simple_term_menu import TerminalMenu
import oinkPackages as oinkPackages
exit = 0
from apps import *
while True:

    cun = oinkPackages.Style.RESET_ALL + userName + "> "
    text = input(cun)
    
    if text == "name":
        
        userName = input("set to ")
    elif text == "help":
            print("commands: name, help, print, exit(can use close), open, meow, python, apps(number app, number app 2, word app), os, desktop, pyrun, text editor")

    elif text == "print":
        toprint = input("text to print ")
        print(toprint)
    elif text == "open":
        file = "drive/" + input("file to open ")
        openedfile = open(file)
        print(openedfile.read())

    elif text == "meow":
        install = input("install program ")
        if install == "extra packages":
            oinkPackages.extra()
        if install == "game player":
            oinkPackages.gamePlayer()
        pass
    elif text == "desktop":
        print("########################################################################################")
        print("#                               desktop kind                                           #")
        print("#                                                                                      #")
        print("#                               A. oink gui 1                                          #")
        print("#                                                                                      #")
        print("#                                                                                      #")
        print("#                                                                                      #")
        print("#                                                                                      #")
        print("#                                                                                      #")
        print("#                                                                                      #")
        print("#                                                                                      #")
        print("#                                                                                      #")
        print("#                                                                                      #")
        print("########################################################################################")
        Answer = input("pick one to use>")
        if Answer == "a" or "A":
            leave = input("press enter to leave")
            if leave == "":
                oinkPackages.os.system("clear")
                print("                                                                 oink os gui 1                                                                                ")
                while True:
                    options = ["exit to shell", "notepad","open file","run python","calculator", "exit"]
                    terminal_menu = TerminalMenu(options)
                    menu_entry_index = terminal_menu.show()
                    if options[menu_entry_index] == "notepad":
                        notepad("drive/" + input("file to wright or make: "))
                    elif options[menu_entry_index] == "exit":
                        exit = 1
                        break
                    elif options[menu_entry_index] == "open file":
                        f = open("drive/" + input("file to open: "), "r")
                        print(f.read())
                    
                    elif options[menu_entry_index] == "calculator":
                        options2 = ["[q]add", "[w]subtract", "[e]multiply", "[r]divide"]
                        terminal_menu = TerminalMenu(options2)
                        menu_entry_index = terminal_menu.show()
                        num1 = int(input("first number: "))
                        num2 = int(input("second number: "))
                        if options2[menu_entry_index] == "[q]add":
                            print(num1 + num2)
                        if options2[menu_entry_index] == "[w]subtract":
                            print(num1 - num2)
                        if options2[menu_entry_index] == "[e]multiply":
                            print(num1 ** num2)
                        if options2[menu_entry_index] == "[r]divide":
                            print(num1 / num2)

                    elif options[menu_entry_index] == "exit to shell":
                        break
                    
                    elif options[menu_entry_index] == "run python":
                        pyFile = input("file name: ")
                        oinkPackages.os.system(f"python3 drive/{pyFile}")


    elif text == "os":
        oinkPackages.os.system(input("command to run "))

    if text == "text editor":
        notepad("drive/" + input("file to wright or make: "))

    elif text == "pyrun":
        pyFile = input("file name: ")
        oinkPackages.os.system(f"python3 drive/{pyFile}")
    #app and games -
    elif text == "python":
        oinkPackages.os.system("python3")

    elif text == "word app":
        while True:
            w = input("Enter a word/ type stop to stop the program: ")
            if w == "stop":
                break
            
            for word in w:
                print(word)



    elif text == "number app 2":
        sum = 0
        while True:
            n = input("Enter a number/ type stop to stop the program: ")
            if n == "stop":
                print(sum)
                break

            else:
                try:
                    sum += int(n)
                except:
                    print("please only enter numbers to exit type stop")

    elif text == "number app":
        num = []
        sum = 0
        for i in range(10):
            num.append(int(input("enter a number: ")))
            


        for i in num:
            sum += i
            

        avrage = sum / 10
        print(f"sum is: {sum}")
        print(f"average is: {avrage}")
    
    #-app and games
    elif exit == 1:
        break
    elif text == "exit":
        break
    elif text == "close":
        break
    elif text == "":
        pass


