
def manager_menu():
    action = ""
    while action != "0":
        print('\nHello Manager !\nWhich action you wanna do?\n\n1 - Edit employee attributes\n2 - Timecard\n3 - Syndicate\n4 - Sales\n0 - Exit')
        action = input('\n')


selection = ""
while selection != "0":
    print('\nHello there !\nWhich section will be chosen?\n\n1 - Add employee\n2 - Remove employee\n3 - Manager.s area\n0 - Exit')
    selection = input('\n')
    if selection == "3":
        manager_menu()

print('\nOkay. See you next time.\nBye')


