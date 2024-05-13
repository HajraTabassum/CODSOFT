import random
import string
plength=int(input("Enter Password length:"))
s1=string.ascii_uppercase
s2=string.ascii_lowercase
s3=string.punctuation
s4=string.digits
l=s1+s2+s3+s4
temp=random.sample(l,plength)
pwd="".join(temp)
print("Password:",pwd)
