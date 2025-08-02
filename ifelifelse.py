
if True:
    print("True")
    print("another line")

input_password = "mypassword"
dbpassword = "mypassword"
admin = True

if input_password == dbpassword:
    print("you are logged in")
elif admin:
    print("you are logged in as admin")
else:
    print("Wrong password")
