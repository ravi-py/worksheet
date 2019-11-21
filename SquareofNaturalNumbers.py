#Program for Difference between the sum of the squares of the first N natural numbers and the square of the sum.

N=int(input("Enter any Natural Number: "))
#The sum of the squares of the first N natural numbers S1
#By using the formula sum of the squares of the first N natural numbers
S1=((N*(N+1)*(2*N+1)))/6
#The square of the sum of the first N natural numbers is S2
#By using the formula The sum of the first N natural numbers
S2=((N*(N+1))/2)**2
#Difference between the sum of the squares of the first N natural numbers and the square of the sum T=S2-S1
T=S2-S1
print("Difference between the sum of the squares of the first N natural numbers and the square of the sum :",T)
