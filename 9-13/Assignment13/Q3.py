def main():
    print("enter marks of the student")
    marks=int(input())
    print("grade:")
    if(marks>=75):
        print("distinction")
    elif(75>marks>=65):
        print("first class") 
    elif(65>marks>=50):
        print("second class")
    elif(marks<50):
        print("fail")    


if __name__=="__main__":
    main()
