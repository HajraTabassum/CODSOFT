print("Calculator")
print("Following are the Operations:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulo Division")
option=int(input("Choose an Option:"))
if(option in [1,2,3,4,5]):
    num1=int(input("Enter the First Number: "))
    num2=int(input("Enter the Second Number: "))
    
    if(option==1):
        result=num1+num2
    elif(option==2):
        result=num1-num2
    elif(option==3):
         result=num1*num2
    elif(option==4):
         result=num1/num2
    elif(option==5):
         result=num1%num2
    else: 
        print("Invalid option")
    print("Result={}".format(result))
