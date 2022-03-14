from week0.christmastree import christmastree
from week0.ship import ship
from week0.keypad import print_matrix
from week0.swap import swap
def f1():
    print('f1')
def f2():
    print('f2')

def buildMenu(menu):
    for key,value in menu.items():
        display = value["display"]
        print(f"{key} ------ {display}")
    print("What is your choice? (enter the number value) ")

def presentMenu(menu):
    buildMenu(menu)
    choice = int(input())
    if (choice) in menu:
        if menu[choice]["type"] == "func":
            menu[choice]["exec"]()
        else:
            presentMenu(menu[choice]["exec"])

subMenu = {
    1: {"display":"f1",
        "exec":f1,
        "type":"func"},
    2: {"display":"f2",
        "type":"func",
        "exec":f2,}
}

mainMenu = {
    1: {"display":"Christmas Tree",
        "exec":christmastree,
        "type":"func"},
    2: {"display":"Ship",
        "exec":ship,
        "type":"func"},
    3: {"display":"Keypad ",
        "exec":print_matrix,
        "type":"func"},
    4: {"display":"Swap ",
        "exec":swap,
        "type":"func"},
    5: {
        "display":"Submenu",
        "exec": subMenu,
        "type":"submenu"
    }
}

if __name__ == "__main__":
    presentMenu(mainMenu)