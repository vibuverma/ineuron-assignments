#-----------------------------------------------------------------------------------------------------
#Answer 1
lst_all_numbers=[]
for x in range(2000, 3201):
    if (x%7==0) and (x%5==0):
        lst_all_numbers.append(str(x))
print (','.join(lst_all_numbers))

#------------------------------------------------------------------------------------------------------
# Answer 2
a= input("Enter First Name :")
b= input("Enter Last Name :")
print("Last Name is: {lastname} and First Name is: {firstname} ".format(firstname=a, lastname=b))

#-------------------------------------------------------------------------------------------------------
# Answer 3
diameter= 12
r= (diameter/2)
volume= (4/3)*3.14*r**3
print("Volume of sphere is : ",volume)
#-------------------------------------------------------------------------------------------------------