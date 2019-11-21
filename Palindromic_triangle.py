#Palindromic triangle
#When we take the N as greater than 9 then  output triangle is not like a Palindromic triangle.
N=int(input("ENTER a natural number N less than 10 :"))
if(0<N<10):
   for i in range(1,N+1):
       print(int('1'*i)**2)
else:
    print("Enter correct natural number which less then 10")