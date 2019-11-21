#Print only Valid email addresses
import re
#From Regular Expressions
regx = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
list = []
n = int(input("Enter number of email Adresses : "))
for i in range(0, n):
    email = input()
    list.append(email)
for j in range (0,n):
    if (re.search(regx, list[j])):
        print(list[j])