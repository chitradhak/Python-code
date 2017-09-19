# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

from datetime import date

'''
x = raw_input("Enter your name: ")
y = input("Enter your age: ")
z = input("Enter current age year: ")
actualyear = (x + ' will turn 100 in year ' + str( z + 100 - y) + '\n' )

print actualyear
'''

############################################################################################

# even / odd number
'''
num1 = input("Enter num 1: ")
def even_odd(num1):
	if num1 % 4 == 0:
		print ("Number is divisble by 4")
	elif num1 % 2 == 0:
		print ("Number is not prime")
	else:
		print("This is a prime number")


even_odd(num1)		

'''

############################################################################################

# write a program that prints out all the elements of the list that are less than 5.
'''
l1 = [56,1,3,8,3,4,10,16,17,80,0.5,5]
l2 = []
l1_len = len(l1)
print l1_len

for i in l1:
	if i <= 5:
		l2.append(i)
print l2
'''
############################################################################################

# palindrome or not.
'''

def palindrom_string():
	x = raw_input("Enter string: ")
	z = x[::-1]
	if x == z:
		print "String is palindrome"
	else:
		print "String is not palindrome"
					
def palindrom_number():
	num = input("Enter num: ")
	sum1=0
	n=num
 
	while num!=0:
		rem=num%10
		sum1=sum1*10+rem
		num=num/10
	if sum1==n:
		print "Number is palindrome"
	else:
		print "Number is not palindrome"	

palindrom_string()
palindrom_number()
'''

############################################################################################

#append tuple indirectly

a = ('2',)
items = ['o', 'k', 'd', 'o']

l = list(a)

for x in items:
    l.append(x)

print tuple(l)



























		 
