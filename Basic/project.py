def validate():
    if  (s_username==uname and s_password==upassword):
        return True
    else:
        return False


s_username="abdulbasith"
s_password="987456"

uname=input("Enter your username")
upassword=input("Enter your password")



a=validate()
print(a)