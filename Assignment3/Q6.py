from sys import getsizeof
def main():
    
    print("enter something")
    x=input()

    print(type(x))
    print(id(x))
    print(getsizeof(x))


if __name__=="__main__":
    main()