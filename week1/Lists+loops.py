
# Hack 1: InfoDB lists.  Build your own/personalized InfoDb with a list length > 3,  create list within a list as illustrated with Owns_Cars

InfoDb = []

InfoDb.append({
    "FirstName": "Lionel",
    "LastName": "Messi",
    "Team": "Paris Saint-Germain F.C.",
    "Ballon d'Ors": "7",
    "Nationality": "Argentina",
    "Played For":["FC Barcelona","Paris Saint-Germain F.C."]
})

InfoDb.append({
    "FirstName": "Cristiano",
    "LastName": "Ronaldo",
    "Team": "Manchester United F.C.",
    "Ballon d'Ors": "5",
    "Nationality": "Argentina",
    "Played For":["Sporting CP","Manchester United F.C.","Real Madrid CF","Juventus F.C."]
})

InfoDb.append({
    "FirstName": "Zlatan",
    "LastName": "Ibrahimović",
    "Team": "A.C. Milan",
    "Ballon d'Ors": "0",
    "Nationality": "Sweden",
    "Played For":["Malmö FF","Ajax","Juventus","Inter Milan","FC Barcelona","AC Milan","Paris Saint-Germain F.C.","Manchester United F.C.","LA Galaxy" ]
})


def print_data(i):
    print(InfoDb[i]["FirstName"], InfoDb[i]["LastName"])  
    print("\t", "Teams Played For: ", end="")  
    print(", ".join(InfoDb[i]["Played For"]))  
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
## hack 2b: def while_loop(0)
## hack 2c : def recursive_loop(0)

def for_loop():
    for i in range(len(InfoDb)):
        print_data(i)

def while_loop(i):
    i = 0
    while i < len(InfoDb):
        print_data(i)
        i += 1
    return


def recursive_loop(i):
    if i < len(InfoDb):
        print_data(i)
        recursive_loop(i+1)
        return



def tester():
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  
    print("Recursive loop")
    recursive_loop(0)  
