#wap that scans an email address and forms a tuple of user name and domain of username
a=input("Enter your email address: ")
if "@" in a:
    b=(a.split("@"))
    i=(b[0],b[1])
    print("User name:",i[0])
    print("Domain:",i[1])
else:
    print("Wrong email address entered")