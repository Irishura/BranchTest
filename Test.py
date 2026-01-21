
# Simple login system

#login credentials
USERNAME = "hadassa"
PASSWORD = "12345"

#inputs
username = input("username : ")
password = input("passwword :")

if username == USERNAME and password == PASSWORD :
    print ("Login Successful!")

else :
    print ("Login Incorrect! Wrong username or password. ")
