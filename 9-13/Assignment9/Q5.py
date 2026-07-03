def main():
    print("enter a number")
    no=int(input())
    if(no%3==0 and no%5==0):
        print(no,"is divisible by 3 and 5")
    else:
        print("number is not divisible by 3 and 5")

if __name__=="__main__":
    main()