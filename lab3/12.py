def is_binary(n):
    if n.isdecimal():
        for i in range(4):
            if n[i]!="0" and n[i]!="1":
                return False
    else:
        return False
    return True   
#------------------------------------------------------   
        
list1=[]
list2=[]
print("To stop input enter -1 ")
while(True):
    txt=input("Enter a binary number of 4 digits : ")
    if txt=="-1":
        break
    elif txt.isdecimal()==False or txt.isalpha()==True:
        print("input is not binary")
    
    elif len(txt)!=4:
        print("invalid size")
    elif is_binary(txt)==True:
        list1.append(txt)
    else:
        print("Number entered in not binary")
    txt=""
for i in list1:
    num=(int(i[3])*(2**3))+(int(i[2])*(2**2))+(int(i[1])*(2**1))+(int(i[0])*(2**0))
    if num%5==0:
        list2.append(i)
print(list2)