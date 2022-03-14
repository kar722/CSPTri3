def swap():
    a = int(input("Enter Your First Number: "))
    b = int(input("Enter You Second Number: "))
    if a > b:
        print(b,a)
    else:
        print(a,b)

if __name__ == "__main__":
    swap()