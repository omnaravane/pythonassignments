def main():
    fact=1
    print("enter a mumber")
    no=int(input())
    for i in range(1,no+1):
        fact=fact*i
    print(fact)

if __name__=="__main__":
    main()
