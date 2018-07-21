x = 1
option = "start"
password = None
count = 0

# while x <= 10:
#     print("%d - Hello" % (x))
#     x+=1

# while option == "start":
#     print("%d - Hello" % (x))
#     x += 1
#     if x > 10:
#         option = "stop"

while password != "abcd1234":
    password = input("Enter password ")
    count += 1

print("password correctly entered in %d attempts" % (count))