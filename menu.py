from functions import manager_menu


selection = ""
while selection != "0":
    print('\nHello there !\nWhich section will be chosen?\n\n1 - Add employee\n2 - Remove employee\n3 - Manager.s area\n0 - Exit')
    selection = input('\n')
    if selection == "1":
        add_employee()

    if selection == "3":
        manager_menu()

print('\nOkay. See you next time.\nBye')