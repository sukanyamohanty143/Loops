import random
print("Guessing Game")
start=input(" ")
chance=int(input("chance:-"))
a=random.randrange(0,9)
#print(a)
i=0
while i<=chance:
	guess=int(input("guess a 1 to 10 number:-"))
	i=i+1
	if guess==a:
		print("correct")
		break
	elif guess<a:
		print("lowest number! try again")
	elif guess>a:
		print("hightest number! try again")
	else:
		print("try again")
		print("Game over")