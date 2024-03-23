num = int(input("enter the number of terms\n "))
n1,n2 = 0,1

count = 0

if num <= 0:
    print ("Please enter a positive integer")
elif num == 1:
    print("The Fibonacci sequence of the numbers up to",num,":")
    print(n1)
else:
    print ("The fibonacci sequence of the numbers is:")
    while count < num:
        print(n1)
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        count += 1