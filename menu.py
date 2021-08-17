from collections import *
from functions import *
from tkinter import *

def menu():
    selection = ""
    while selection != "0":
        print('\nHello there !\nWhich section will be chosen?\n\n1 - Add employee\n2 - Remove employee\n3 - Manager´s area\n4 - Rotate Schedule\n5 - Payment Schedule\n6 - New Schedule\n0 - Exit')
        selection = input('\n')
        if selection == "1":
            Add_Employee()

        if selection == "2":
            Remove_Employee()

        if selection == "3":
            Manegers_Menu()
    
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