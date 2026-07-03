#program to accept 2 numbers and check the greater number
def chkgreater(value1,value2):
    if(value1>value2):
         return True
    else:
        return False

def main():
    no1=int(input("enter first number"))
    no2=int(input("enter second number"))

    ret=chkgreater(no1,no2)
    if (ret==True):
        print(no1,"is greater")
    else:
         print(no2,"is greater")



if __name__=="__main__":
    main()