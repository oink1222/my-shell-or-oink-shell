from simple_term_menu import TerminalMenu

def notepad(file):
    f = open(file, "a")
    f.write(input("text for file: "))
    f.close()
def fileExoplorer():

    import os

    
    files = os.listdir('drive/')
    terminal_menu = TerminalMenu(files)
    menu_entry_index = terminal_menu.show()
    options = ["[a]open", "[s]run with python", "[q]exit"] 
    f = options[menu_entry_index]
    terminal_menu = TerminalMenu(options)
    fileoptions = terminal_menu.show()
    if {options[fileoptions]} == "run with python":
        pyFile = f
        os.system(f"python3 drive/{pyFile}")
    if {options[fileoptions]} == open:
        print(f.read())
    if {options[fileoptions]} == exit:
        pass

