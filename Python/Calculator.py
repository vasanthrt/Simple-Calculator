def add(e,v):
   return(e+v)

def sub(e,v):
   return(e-v)

def mul(e,v):
   return(e*v)

def div(e,v):
   return(e/v)

def rem(e,v):
   return(e%v)



print("1)add")
print("2)sub")
print("3)mul")
print("4)div")
a=input("enter your choice:")
if a==1:
   a = input("first number\n")
   b = input("second number\n")
   print"sum =",add(a,b)
elif a==2:
   a = input("first number\n")
   b = input("second number\n")
   print"difference =",sub(a,b)

elif a==3:
   a = input("first number\n")
   b = input("second number\n")
   print"product =",mul(a,b)

elif a==4:
   a = input("first number\n")
   b = input("second number\n")
   print"quotient =",div(a,b)
   print"remainder =",rem(a,b)
   
else :
   print("invalid choice\n")

"""
Project Name: Simple Calculator
Created by  : Vasanth R
Date        : 28/12/2018
Time        : 10:23 AM (IST)
"""
