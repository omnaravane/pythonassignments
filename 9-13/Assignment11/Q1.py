def chkprime(value):
      for i in range(2,value):
        if(value%i==0): 
           return True
    
def main():
    print("enter a number")
    no=int(input())
    ret=chkprime(no)
    if(ret==True):
        print("number is not prime")
    else:
        print("number is prime")
   
if __name__=="__main__":
    main()