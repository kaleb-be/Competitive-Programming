#!/bin/python3

def dominoPiling(m, n):
    return (m*n)//2

if __name__ == '__main__':
    m = int(input("Enter the width of the board: ").strip())
    print(m)
    n = int(input("Enter the height of the board: ").strip())
    print(m)
    optimalPile= dominoPiling(m,n)
    print(f"The maximum number of dominoes is: {optimalPile}")
