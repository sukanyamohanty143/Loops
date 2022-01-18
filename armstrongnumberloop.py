i=int(input("enter a number"))
num=num1=i
count=0
sum=0
while num1>0:
	count=count+1
	num1=num1//10
while i>0:
	digit=i%10
	r=digit**count
	sum=sum+r
	i=i//10
if sum==num:
	print("number is armstrong number")
else:
	print("number is not a armstrong number")