class Multiple_Functions:
    def BMI():
        bmi=float(input("Enter the BMI Index: "))
        print("The BMI Index : ",bmi)
        if bmi < 18.5:
            print("Under Weight")
        elif 18.5 <= bmi and bmi <= 24.9:
            print("Normal Weight")
        elif 25.0 <= bmi and bmi <= 29.9:
            print("Over Weight")
        elif 30.0 <= bmi and bmi <= 34.9:
            print("Obese Class 1")
        elif 35.0 <= bmi and bmi <= 39.9:
            print("Obese Class 2")
        else:
            print("Obese Class 3")
            
    def Add():
        #Addition
        a=int(input("a = "))
        b=int(input("b = "))
        print("a : ",a)
        print("b : ",b)
        print("Add = ",a+b)
        
    def Sub():
        #Subtraction
        a=int(input("a = "))
        b=int(input("b = "))
        print("a : ",a)
        print("b : ",b)
        print("Sub = ",a-b)
        
    def Mul():
        #Multiplication
        a=int(input("a = "))
        b=int(input("b = "))
        print("a : ",a)
        print("b : ",b)
        print("Mul = ",a*b)
        
    def Div():
        #Division
        a=int(input("a = "))
        b=int(input("b = "))
        print("a : ",a)
        print("b : ",b)
        print("Float Div = ",a/b)
        
    def Floor_Div():
        #Floor Division
        a=int(input("a = "))
        b=int(input("b = "))
        print("a : ",a)
        print("b : ",b)
        print("Floor Div = ",a//b)
        
    def Modulo():
        #Modulo
        a=int(input("a = "))
        b=int(input("b = "))
        print("a : ",a)
        print("b : ",b)
        print("Modulo = ",a%b)
        
    def Power():
        #Power
        a=int(input("a = "))
        b=int(input("b = "))
        print("a : ",a)
        print("b : ",b)
        print("Power = ",a**b)
        
    def Age_Category():
        # Category the people by their age like children, adult, citizen, senior citizen
        age = int(input("age : "))
        print("The age is ",age)
        if age < 18:
            print("Children")
        elif age >= 18 and age < 35:
            print("Adult")
        elif age >= 35 and age < 60:
            print("Citizen")
        else:
            print("Senior Citizen")
            
    def Num_Check():
        # Find whether given number is positive or negative
        a = int(input("Enter any number : "))
        print("The Number is ",a)
        if a == 0:
            print("Numer is zero")
        elif a < 0:
            print("Number is Negative")
        else:
            print("Number is Positive")
            
    def Subfields():
        print("Sub-fields in AI are :")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")
        
    def OddEven():
        a = int(input("Enter a number: "))
        print("The Number is ",a)
        if a%2 == 0:
            print(a, "is Even number")
        else:
            print(a, "is Odd number")
            
    def Eligible_For_Marriage():
        Gender = input("Your Gender : ")
        Age = int(input("Your Age : "))
        print("The Gender is ",Gender)
        print("The Age is ",Age)
        if Gender == "Male":
            if Age >= 21:
                print("Elgible")
            else:
                print("Not Eligile")
        else:
            if Age >= 18:
                print("Elgible")
            else:
                print("Not Eligile")
                
    def percentage():
        S1=int(input("Subject 1 : "))
        S2=int(input("Subject 2 : "))
        S3=int(input("Subject 3 : "))
        S4=int(input("Subject 4 : "))
        S5=int(input("Subject 5 : "))

        print("The subject 1 is ",S1)
        print("The subject 1 is ",S2)
        print("The subject 1 is ",S3)
        print("The subject 1 is ",S4)
        print("The subject 1 is ",S5)

        Total = S1+S2+S3+S4+S5
        percentage = (Total * 100)/500
        print("Total : ",Total)
        print("Percentage : ",percentage)
        
    def Area_of_triange():
        Height=int(input("Height : "))
        Breadth=int(input("Breadth : "))
        print("The Height is ",Height)
        print("The Breadth is ",Breadth)
        print("Area formula: (Height*Breadth)/2")
        Area = (Height*Breadth)/2
        print("Area of Triangle : ",Area)
        
    def Perimeter_of_triangle():
        Height1=int(input("Height1 : "))
        Height2=int(input("Height2 : "))
        Breadth1=int(input("Breadth1 : "))
        print("The Height1 is ",Height1)
        print("The Height2 is ",Height2)
        print("The Breadth1 is ",Breadth1)
        print("Perimeter formula: Height1+Height2+Breadth1")
        Perimeter = Height1+Height2+Breadth1
        print("Perimeter of Triangle : ",Perimeter)