from week0.christmastree import christmastree
from week0.ship import ship
from week0.keypad import print_matrix
from week0.swap import swap

from week1.fibonacci import fibo_print
from week1.Listsloops import ll

from week2.factorial import printfac
from week2.mathfunc import trian
from week2.palindrome import pal



week0 = {
    1: {
        "display":"Christmas Tree",
        "exec":christmastree,
        "type":"func"
    },
    2: {
        "display":"Ship",
        "exec":ship,
        "type":"func"},
    3: {
        "display":"Keypad ",
        "exec":print_matrix,
        "type":"func"},
    4: {
        "display":"Swap ",
        "exec":swap,
        "type":"func"},
    0: {
        "display": "Quit",
        "exec":quit,
        "type":"func"
    }
}
week1 = {
  1: {
    "display": "Fibonacci",
    "exec": fibo_print,
    "type": "func"
  },
  2: {
    "display": "Lists & Loops",
    "exec": ll,
    "type": "func"
  },
  0: {
    "display": "Quit",
    "exec": quit,
    "type": "func"
  }
}
week2 = {
    1: {
        "display":"Factorial",
        "exec":printfac,
        "type":"func"
    },
    2: {
        "display":"Math Function: Triangular Numbers",
        "exec":trian,
        "type":"func"
    },
    3: {
        "display":"EC: Palindrome",
        "exec":pal,
        "type":"func"
    },
    0: {
        "display":"Quit",
        "exec":quit,
        "type":"func"
    }
}

mainMenu = {
    1: {
        "display": "Week 0",
        "exec": week0,
        "type": "submenu"
    },
    2: {
        "display": "Week 1",
        "exec": week1,
        "type": "submenu"
    },
    3: {
        "display": "Week 2",
        "exec": week2,
        "type": "submenu"
    },

    0: {
        "display": "Quit",
        "exec":quit,
        "type":"func"
    }
}


def buildMenu(menu):
    for key,value in menu.items(): 
        display = value["display"]
        print(f"{key} ------ {display}") # each menu item is printed
    print("What is your choice? (enter the number value) ") # user input promp

def presentMenu(menu):
    buildMenu(menu) #print out menu and take input
    choice = int(input())
    while choice not in menu: # ensure that choice is valid
        choice = int(input("Please elect a valid item. "))
    if (choice) in menu:
        if menu[choice]["type"] == "func": #determine whether recursion is needed
            menu[choice]["exec"]() #run function

        else:
            presentMenu(menu[choice]["exec"]) #display submenu

if __name__ == "__main__":
  while True:
    presentMenu(mainMenu)



