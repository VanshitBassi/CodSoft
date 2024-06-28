#Create a simple Claculator by using a python:
print("Take two inputs from the user")
a1 = (int(input("Enter the first number: ")))
b2 = (int(input("Enter the second number: ")))

choice=0
# While loop is use for continue running the "Calculation" till to thce 5 but stop at 6.
while choice<6:

#Arithmetic operators:                   
                    print("1.Add")
                    print("2.Subtraction")
                    print("3.Multiplication")
                    print("4.Divide")
                    choice =(int(input("Enter the choice:")))

#Conditional statements are used in simple Python calculators to control the flow of the program                
                    if choice == 1:
                            c3 = a1 + b2
                            print('Sum:', c3)
                    elif choice == 2:
                            c3 = a1 - b2
                            print('Difference:', c3)
                    elif choice == 3:
                            c3 = a1 * b2 
                            print('product:', c3)    
                    elif choice == 4:
                            c3 = a1 / b2
                            print('quotent:', c3)
                    elif choice == 6:
                           break       
                    else:
                            print('The syntax is Invalid')   



     