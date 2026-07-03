def main():
    no=int(input("enter a number"))
    for no in range(no+1):
        if(no%2==0):
            print(no)

if __name__=="__main__":
    main()