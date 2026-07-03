def main():
    no=int(input("enter a number"))
    for i in range(1,no+1):
        if (no%i==0):
            print(i)    

if __name__=="__main__":
    main()