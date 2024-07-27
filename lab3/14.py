password=input("Enter New Password ")
check=1
symbol=0
digit=0
small_alpha=0
capital_alpha=0
list1=['$','#','@']
if len(password)<6 or len(password)>16:
    print("Invalid Password length ")
else:
    for i in range(len(password)):
        temp=password[i]
        if temp in list1:
            symbol+=1
        elif temp.isdigit()==True:
            digit+=1
        elif temp==temp.lower():
            small_alpha+=1
        elif temp==temp.upper():
            capital_alpha+=1
    if symbol==0:
        print("password must contain one of these ",list1)
        check=-1
    if digit==0:
        print("password must contain atleast 1 digit")
        check=-1
    if small_alpha==0:
        print("password must contain atleast 1 small alphabet")
        check=-1
    if capital_alpha==0:
        print("password must contain atleast 1 capital alphabet")
        check=-1
    if check==-1:
        print("Invalid Password ")
    else:
        print("Valid Password")
    print(symbol)
    print(digit)
    print(small_alpha)
    print(capital_alpha)
    print(check)