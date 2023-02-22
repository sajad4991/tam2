a = input("first name :")
for i in range(len(a)):
    if a[i] == '0' or a[i] == '1' or a[i] == '2' or a[i] == '3' or a[i] == '4' or a[i] == '5' or a[i] == '6' or a[i] == '7' or a[i] == '8' or a[i] == '9':
        print("num in first name is wrong ! ")
    exit(1)
b = input("last name :")
for j in range(len(b)):
     if b[j] == '0' or b[j] == '1' or b[j] == '2' or b[j] == '3' or b[j] == '4' or b[j] == '5' or b[j] == '6' or b[j] == '7' or b[j] == '8' or b[j] == '9':
        print("num in last name is wrong ! ")
        exit(1)   
c = input("Postal code :")
if len(c) != 10:
    print("the length of postalcode should be 10 ")
    exit(1)
d = input("cell number :")
if d[0] != '0' or d[1] != '9':
    print("the phone number shoold start with 09 ")
    exit(1)
e = input("email address :")
for k in range(1,len(e)):
    if e[k] == '@':
        print("thanks for your information")
        break
    else:
        print("the email address shuld include @")
