def print_matrix():
    matrix = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
    for x in matrix:
        print(*x)


  

if __name__ == "__main__":
    print_matrix([[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]])