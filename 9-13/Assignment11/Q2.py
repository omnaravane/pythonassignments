def main():
    
    print("enter a number")
    no=int(input())
    sum=0
    while no > 0:
        digit=no % 10
        sum=sum+digit
        no = no // 10
    print(sum)
    
if __name__=="__main__":
    main()