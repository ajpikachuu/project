num= input("enter the num: ")
num1=len(num)
num=int(num)
num2=num 
sum = 0
while(num>0):
    d = num%10
    sum=sum+d**num1
    num=num//10
if(sum==num2):
    print("Armstrong Number!")
else:
    print("Not an Armstrong Number!")