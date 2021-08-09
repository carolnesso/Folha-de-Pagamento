import collections
from functions import *
from tkinter import *

def menu():
    selection = ""
    while selection != "0":
        print('\nHello there !\nWhich section will be chosen?\n\n1 - Add employee\n2 - Remove employee\n3 - Manager´s area\n4 - Rotate Schedule\n5 - Payment Schedule\n6 - New Schedule\n0 - Exit')
        selection = input('\n')
        if selection == "1":
            add_Employee()

        if selection == "2":
            #remove_employee
            pass

        if selection == "3":
            action = ""
            while action != "0":
                print('\nHello Manager !\nWhich action you wanna do?\n\n1 - Edit employee attributes\n2 - Timecard\n3 - Syndicate\n4 - Sales\n5 - Undo/Redo\n0 - Exit')
                action = input('\n')

        if selection == "4":
            #rodar_folha_de_pagamento
            pass

        if selection == "5":
            #agenda_de_pagamento()
            pass

        if selection =="6":
            #criar_nova_agenda
            pass

    print('\nOkay. See you next time.\nBye')

menu()

#window = Tk()
#window.title("Folha de Pagamento")
#textmenu = Label(window, text="Hello there ! \nClick down below to start the program.\n")
#textmenu.grid(column=0, row=0)
#press = Button(window, text="Start", command= menu)
#press.grid(column=0, row=1)
#window.mainloop()