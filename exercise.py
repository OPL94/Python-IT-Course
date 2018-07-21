#Exercise 1
# print('''Bob
# ST1001
# bob@gmail.com''')

#Exercise 2
# print("%d + %d = %d" % (14,7,14+7))
# print("%d * %d = %d" % (14,7,14*7))
# print("%d - %d = %d" % (14,7,14-7))
# print("%d / %d = %d" % (14,7,14//7))

#Exercise 3
# for x in range(1,6):
#     print("\t" * (x-1) + str(x))

#Exercise 4
# print('''"SDK" stands for "Software Development Kit", whereas
# "IDE" stands for "Integrated Development Environment".''')

#Exercise 5
# YOB = int(input("You are born in "))
# print('''You are born in %d.
# In year 2020, you will be %d years old''' % (YOB,2020-YOB))

#Exercise 6
# name = input("Please enter your name: ")
# print("Hi %s, welcome to Python Programming :)" % (name))

#Exercise 11
# first = input("Please enter your first name: ")
# last = input("Please enter your last name: ")
#
# print("Your full name is %s %s" % (first.upper(),last.upper()))
# print("Your initials are %s %s" % (first[0].upper(),last[0].upper()))
# print("First name length is %d letters" % (len(first)))
# print("Last name length is %d letters" % (len(last)))
# print("Full name length is %d letters" % (len(first)+len(last)))
# print("First name starts with %s" % (first[0].upper()))
# print("First name ends with %s" % (first[-1].upper()))
# print("Last name starts with %s" % (last[0].upper()))
# print("Last name ends with %s" % (last[-1].upper()))
# print("First name indexes are %d - %d" % (0,len(first)-1))
# print("Last name indexes are %d - %d" % (0,len(last)-1))
# print("First name trims 1 %s" % (first[0:3]))
# print("First name trims 2 %s" % (first[1:]))
# print("Last name trims 1 %s" % (last[0:3]))
# print("Last name trims 2 %s" % (last[3:]))


#Exercise 12
# month_by_num = {
#     "1": "January",
#     "2": "February",
#     "3": "March",
#     "4": "April",
#     "5": "May",
#     "6": "June",
#     "7": "July",
#     "8": "August",
#     "9": "September",
#     "10": "October",
#     "11": "November",
#     "12": "December"
#
# }
#
# month = input("Enter a month: ")
# print("Month %s is %s" % (month,month_by_num[month]))


#Exercise 13

#Number = int(input("Enter a number "))
# if Number % 2 == 0:
#     print("%d is even" % (Number))
# else:
#     print("%d is odd" % (Number))

#Exercise 14
# price = 6
#
# age = int(input("Enter your age "))
#
# if age < 16:
#     print("Your ticket costs £%.2f" % (price/2))
# elif age >= 60:
#     print("Your ticket costs £%.2f" % (price/3))
# else:
#     print("Your ticket costs £%.2f" % (price))

#Exercise 16

# comedy = input("Would you like to see a comedy (yes/no)? ")
#
# if comedy == "yes":
#     print("You might like either Yes Minister or SPAMalot")
# else:
#     musical = input("Would you like to see a musical (yes/no)? ")
#     if musical == "yes":
#         print("You might like either The Woman in Black or Macbeth")
#     else:
#         horror = input("Would you like to see a horror (yes/no)? ")
#         if horror == "yes":
#             print("You might like either Les Miserables or Mamma Mia")

#Exercise 17
# for x in range(10):
#     print(x)

#Exercise 18
# for x in range(9,-1,-1):
#     print(x)

#Exercise 19

# for x in range(1,6):
#     print("* " * x)


#Exercise 20

# for x in range(1,10):
#     if x % 3 == 0:
#         print(x)
#     else:
#         print(x, end='\t')

#Exercise 21 Encrypt Name

# name = input("Please enter your name: ")
#
# num_name = len(name)
#
# print("Encrypted form is %s %s %s" % (name[0], (num_name-2) * "*",name[-1]))



#Exercise 22

# famount = int(input("Enter the first amount in Celcius: "))
# lamount = int(input("Enter the last amount in Celcius: "))
#
#
# print("CELCIUS %s FAHRENHEIT" % ('\t'))
#
# for x in range(famount,lamount + 1):
#     print("%d %s %.1f" % (x, '\t'*3,(x*9/5) + 32))







