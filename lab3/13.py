letters=0
digits=0

txt=input("Write a alphanumeric string : ")
for i in range(len(txt)):
    if txt[i].isalpha():
        letters+=1
    elif txt[i].isdigit():
        digits+=1
print("Letters : ",letters)
print("digits : ",digits)