class multiopeartion():
    #Create Function List out the item list
    def Subfields():
        print('\n'.join(['Sub-Fields in AI are:', 'Machine learning','Neural Networks','Vision','Robotics','Speech processing','Natural language processing'] ))

#Function to check whether given number is odd or even
    def OddorEven():
        num1=int(input("Enter a number"))
        print(f"{num1}  {'odd number' if num1 / 2 == 0 else 'is Even Number'}")

#Eligible for marraige Male or Female
    def Eligible(age:int,gender:str):
        print(f"Your Gender:{ gender } \n Your Age :{ age }")
        print('ELIGIBLE'     if ( gender == 'Male' and age >= 21 ) else 
              'NOT ELIGIBLE' if ( gender == 'Male' and age <= 21 ) else 
              'ELIGIBLE'     if ( gender == 'female' and age >= 18 ) else 
              'NOT ELIGIBLE' if ( gender == 'female' and age <= 18 ) else ' ')
   
#Calculate percentage of 10 th mark
    def percentage(*args):
        total = 0
        for sub in args:
            total = total + sub
            per = total/len(args)
        return total,per

#Eligible for marraige Male or Female
    def Traingle(*args):
        h1,h2,b1 = args
        area = lambda h1,b1: h1*b1/2
        peri = lambda h1,h2,b1: h1+h2+b1/3
        return area(h1,b1),peri(h1,h2,b1)