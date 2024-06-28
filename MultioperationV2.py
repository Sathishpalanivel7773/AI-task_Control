class multiopeartion():
    #Create Function List out the item list
    def Subfields():
        print('\n'.join(['Sub-Fields in AI are:', 'Machine learning','Neural Networks','Vision','Robotics','Speech processing','Natural language processing'] ))

#Function to check whether given number is odd or even
    def OddorEven():
        num1=int(input("Enter a number"))
        print(f"{num1}  {'odd number' if num1 / 2 == 0 else 'is Even Number'}")

#Eligible for marraige Male or Female
    def Eligible():
        age = int(input('Enter input age: '))
        gender = str(input('Enter gender: '))
        print(f"Your Gender:{ gender } \n Your Age :{ age }")
        print('ELIGIBLE'     if ( gender == 'Male' and age >= 21 ) else 
              'NOT ELIGIBLE' if ( gender == 'Male' and age <= 21 ) else 
              'ELIGIBLE'     if ( gender == 'female' and age >= 18 ) else 
              'NOT ELIGIBLE' if ( gender == 'female' and age <= 18 ) else ' ')
   
#Calculate percentage of 10 th mark
    def percentage():
        sub1,sub2,sub3,sub4,sub5 = map(int,input( "Enter mark:Sub1,sub2,sub3,sub4,sub5:").split())
        total = sub1+sub2+sub3+sub4+sub5
        per = total/5
        print(f"Subject1 = { sub1 }\n Subject2 = { sub2 } \n Subject3 = { sub3 } \n Subject4 = { sub4 }\n Subject5 = { sub5 } \n Total : { total } \n Percentage : { per }")   
        

#Eligible for marraige Male or Female
    def Traingle():
        h1,h2,b1 = map(int,input( "Enter mark:height1,height2,breadth:").split())
        area =  h1*b1/2 
        peri =  (h1+h2+b1)/3 
        print(f"Height:{ h1 } \n breadth : { b1 } \n Area of formula:(Height*breadth/2) \n Area of Triangle: { area }\n Height1:{ h1 } \n Height2:{ h2 }\n breadth: { b1 } \n perimeter formula:Height1+Height2+Breadth\n Perimeter of triangle { peri },")