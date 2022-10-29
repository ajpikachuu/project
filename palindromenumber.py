n=int(input("enter the number: "))
n1=n
reverse=0
while (n > 0):
    reminder=n%10
    reverse=reverse*10+reminder
    n=n//10
if (reverse==n1):
    print("the number is palindrome")
else:
    print("the number is not palindrome")


